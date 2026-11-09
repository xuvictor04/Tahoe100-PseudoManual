---
symbol: "SLC43A3"
type: "gene"
col: 5606
ensembl_id: "ENSG00000134802"
name: "solute carrier family 43 member 3"
location: "11q12.1"
module: 112
arm: "+"
pooled_cpm: 19.46
n_lines_expressing: 22
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 22
direction_downstream: 30
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# SLC43A3

*solute carrier family 43 member 3* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.81× (z +7.4, q 6e-11, up in 9 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.86× (z +5.5, q 3e-06, up in 5 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.506× (z -8.5, q 8e-15, down in 19 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR155HG]] (+0.64, fdr 7e-06), [[MIR3142HG]] (+0.60, fdr 1e-05), [[GYPC]] (+0.58, fdr 1e-05); moves opposite to [[SPAST]] (-0.42, fdr 9e-05), [[ADD1]] (-0.42, fdr 1e-04), [[WWP1]] (-0.42, fdr 2e-04).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[ZFPM2-AS1]] → it (grade B ⚠); 30 go from it, the strongest it → [[GPR68]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.4 | 6e-11 | 9/19 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.50×** | +7.1 | 3e-10 | 10/20 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.1 | 3e-10 | 2/16 (KATO III, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.7 | 4e-09 | 4/20 (KATO III, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.61×** | +6.0 | 3e-07 | 11/20 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +5.5 | 3e-06 | 5/20 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +4.9 | 6e-05 | 2/18 (KATO III, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 4/20 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.004 | 16/20 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.005 | 12/20 (HOP62, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.007 | 7/20 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.36×** | +3.7 | 0.009 | 5/19 (NCI-H2347, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.36×** | +3.7 | 0.009 | 14/20 (SNU-423, hTERT-HPNE, …) | rises with dose | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.021 | 2/20 (NCI-H1792, LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.32×** | +3.4 | 0.023 | 7/20 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.036 | 2/20 (HS-578T, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.042 | 13/20 (J82, Panc 03.27, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.067 | 3/20 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -8.5 | 8e-15 | 19/20 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -6.7 | 8e-09 | 20/20 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -5.5 | 8e-06 | 15/20 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.681×** | -4.5 | 0.001 | 11/20 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.701×** | -4.1 | 0.004 | 4/20 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.545×** | -4.0 | 0.006 | 9/20 (C32, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.731×** | -3.9 | 0.007 | 8/19 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.007 | 10/20 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.726×** | -3.7 | 0.012 | 0/20 | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.568×** | -3.7 | 0.012 | 14/20 (C32, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.05 µM |  | **0.768×** | -3.3 | 0.048 | 5/20 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.777× | -3.0 | 0.11 | 9/20 (H4, J82, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.632× | -3.0 | 0.11 | 13/20 (SNU-423, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 139 | 2 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +18.7) ⚠ cell-cycle shift, explains ~56% of this change | [[Panobinostat (drug)]] 5 µM 0.154× (z -18.4) |
| [[NCI-H1792 (line)]] | alt | 146 | 1 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.61× (z +9.0) ⚠ cell-cycle shift, explains ~60% of this change | [[Dinaciclib (drug)]] 5 µM 0.197× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.285× (z -12.2) |
| [[A-172 (line)]] | wt | 18.0 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +16.8) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 8.45× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 78.7 | 3 (3 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 5.14× (z +12.0) ⚠ cell-cycle shift, explains ~60% of this change | [[Panobinostat (drug)]] 5 µM 0.177× (z -13.2) |
| [[C32 (line)]] | wt | 58.4 | 0 | 4 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.215× (z -10.9) |
| [[HS-578T (line)]] | alt | 8.37 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +13.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 7.36× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 76.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 53.4 | 1 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.71× (z +8.5) ⚠ cell-cycle shift, explains ~60% of this change | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -10.4) |
| [[HOP62 (line)]] | alt | 41.8 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.1) ⚠ cell-cycle shift, explains ~56% of this change | [[Panobinostat (drug)]] 5 µM 0.291× (z -9.6) |
| [[J82 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +15.8) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 7.82 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +12.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[H4 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[KATO III (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2347 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +9.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW 900 (line)]] | alt | 59.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -9.0) |
| [[SW480 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -13.8) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-427 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR155HG]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[MIR3142HG]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GYPC]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[C1QTNF1]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CDH13]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CSF2]] | +0.53 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[RUNX3]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[NGF]] | +0.51 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[MME]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[IL1A]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAST]] | -0.42 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[ADD1]] | -0.42 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[WWP1]] | -0.42 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[PHKB]] | -0.41 | -0.31 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 4, C 18. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFPM2-AS1]] | B | ZFPM2-AS1 activity raises SLC43A3's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without ZFPM2-AS1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[LINC02454]] | B | LINC02454 activity raises SLC43A3's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.77× lower at baseline in the lines without LINC02454 | 0.079 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[GATM]] | B | GATM activity lowers SLC43A3's level | lines that do not express GATM (7) vs lines expressing it (43) | 2.65× higher at baseline in the lines without GATM | 0.090 | ⚠ within organs, on part of the lines; also absent: CTSH, KIAA1522; maybe low, not absent |
| [[NFATC2]] | B | NFATC2 activity raises SLC43A3's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 3.19× lower at baseline in the lines without NFATC2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[MIR155HG]] | C | MIR155HG activity raises SLC43A3's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 3.83× lower at baseline in the lines without MIR155HG | 0.001 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; co-absent with the target |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises SLC43A3's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 4.78× lower at baseline in the lines without ROR1-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |
| [[IL6]] | C | IL6 activity raises SLC43A3's level | lines that do not express IL6 (32) vs lines expressing it (18) | 4.66× lower at baseline in the lines without IL6 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[PLPP4]] | C | PLPP4 activity raises SLC43A3's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 6.03× lower at baseline in the lines without PLPP4 | 0.006 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6; co-absent with the target |
| [[EVA1A]] | C | EVA1A activity raises SLC43A3's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 4.77× lower at baseline in the lines without EVA1A | 0.007 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[G0S2]] | C | G0S2 activity raises SLC43A3's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 3.42× lower at baseline in the lines without G0S2 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises SLC43A3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 5.67× lower at baseline in the lines without CDH13 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises SLC43A3's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.83× lower at baseline in the lines without FRMD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 11, C 19. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR68]] | B | SLC43A3 activity raises GPR68's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without SLC43A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[ZNF697]] | B | SLC43A3 activity raises ZNF697's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without SLC43A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[NFATC2]] | B | SLC43A3 activity raises NFATC2's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without SLC43A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[IKBKE]] | B | SLC43A3 activity raises IKBKE's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without SLC43A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[RASSF5]] | B | SLC43A3 activity raises RASSF5's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without SLC43A3 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[RUNX1]] | B | SLC43A3 activity raises RUNX1's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without SLC43A3 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[PPIF]] | B | SLC43A3 activity raises PPIF's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without SLC43A3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[MFSD2A]] | B | SLC43A3 activity strengthens MFSD2A's drug response | lines that do not express SLC43A3 (27) vs lines expressing it (19) | the lines without SLC43A3 respond 0.75× as strongly (z diff +1.03); strongest at Homoharringtonine 0.5 µM: 4.16x vs 10x (z diff +2.6) | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; target measured in part of the lines; artifact flags |
| cells under [[Belumosudil (drug)]] 5 µM | B | SLC43A3 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express SLC43A3 (28) vs lines expressing it (20) | the lines without SLC43A3: 0.71× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[LINC02454]] | B | SLC43A3 activity raises LINC02454's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without SLC43A3 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[TNFRSF1B]] | B | SLC43A3 activity raises TNFRSF1B's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without SLC43A3 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[EVA1A]] | C | SLC43A3 activity raises EVA1A's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without SLC43A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, 1.0); signed map (41.3, 13.4). **Vector** length 75.1, 23.7% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.3 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +0.9 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 43 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,406,954-57,427,580 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEEEG-1, Eeg1, DKFZp762A227, FOAP-13, PRO1659 |
| Gene groups (HGNC) | Solute carrier family 43 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBI5](https://www.uniprot.org/uniprotkb/Q8NBI5) (Equilibrative nucleobase transporter 1):

> Sodium-independent purine-selective nucleobase transporter which mediates the equilibrative transport of extracellular purine nucleobases such as adenine, guanine and hypoxanthine. May regulate fatty acid (FA) transport in adipocytes, acting as a positive regulator of FA efflux and as a negative regulator of FA uptake (By similarity).; [Isoform 1]: Sodium-independent purine-selective nucleobase transporter which mediates the equilibrative transport of extracellular purine nucleobase adenine. …

**Summary**, from NCBI Gene [29015](https://www.ncbi.nlm.nih.gov/gene/29015):

> Enables adenine transmembrane transporter activity; guanine transmembrane transporter activity; and xenobiotic transmembrane transporter activity. Involved in hypoxanthine transport. Located in basolateral plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17466) · Entrez [29015](https://www.ncbi.nlm.nih.gov/gene/29015) · UniProt [Q8NBI5](https://www.uniprot.org/uniprotkb/Q8NBI5) · Ensembl [ENSG00000134802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134802)

## Data

Gene col 5606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5606); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5606]; `tensor/DDL_lfc|DDL_z.npy` [5606]; `embed/gene_vectors.npy` [5606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5606 or target_col == 5606). Every well: [[SLC43A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC43A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

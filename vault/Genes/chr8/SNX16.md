---
symbol: "SNX16"
type: "gene"
col: 2467
ensembl_id: "ENSG00000104497"
name: "sorting nexin 16"
location: "8q21.13"
module: 199
arm: "+"
pooled_cpm: 17.74
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# SNX16

*sorting nexin 16* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.28× (z +23.2, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.714× (z -4.8, q 5e-04, down in 16 of 45 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEAL1]] (+0.61, fdr 6e-05), [[MATCAP2]] (+0.60, fdr 1e-05), [[TET2]] (+0.58, fdr 2e-04); moves opposite to [[ZMYND19]] (-0.62, fdr 3e-05), [[NUP93]] (-0.60, fdr 7e-05), [[WDR5]] (-0.60, fdr 2e-04).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HMGN5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +23.2 | 0e+00 | 41/47 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +11.2 | 1e-26 | 32/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +8.9 | 1e-16 | 25/48 (NCI-H2347, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.7 | 3e-16 | 28/47 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +8.2 | 3e-14 | 25/47 (NCI-H2347, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +7.5 | 6e-12 | 22/44 (SW 900, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +6.7 | 2e-09 | 25/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +5.6 | 2e-06 | 19/47 (A498, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 3e-06 | 17/47 (HOP62, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.4 | 4e-06 | 14/47 (HEC-1-A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +5.3 | 6e-06 | 18/47 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.3 | 6e-06 | 16/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.1 | 1e-05 | 14/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 2e-05 | 15/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.31×** | +5.0 | 2e-05 | 12/48 (A498, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 3e-05 | 17/47 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.28×** | +4.8 | 4e-05 | 10/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.002 | 11/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 8/48 (A498, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.714×** | -4.8 | 5e-04 | 16/45 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.787×** | -4.8 | 5e-04 | 15/44 (RPMI-7951, AN3 CA, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.783×** | -4.7 | 5e-04 | 14/47 (RKO, NCI-H1792, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.812×** | -4.2 | 0.005 | 12/45 (COLO 205, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.763×** | -3.8 | 0.012 | 10/47 (SHP-77, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.825×** | -3.8 | 0.012 | 15/42 (A-427, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.771×** | -3.7 | 0.017 | 9/46 (HT-29, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.836× | -3.6 | 0.025 | 9/47 (SW480, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 12.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.5) | — |
| [[A498 (line)]] | wt | 20.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.0) | — |
| [[KATO III (line)]] | alt | 19.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 18.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 21.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 28.9 | 1 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.39× (z +11.3) | [[Tubulin inhibitor 6 (drug)]] 0.5 µM 0.254× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 7.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +17.3) | — |
| [[RKO (line)]] | wt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 15.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[A-172 (line)]] | wt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +13.7) | — |
| [[A-427 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 9.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.5) | — |
| [[LoVo (line)]] | wt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEAL1]] | +0.61 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[MATCAP2]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TET2]] | +0.58 | +0.47 / +0.32 | both halves | 2e-04 |  |
| [[DNAJB4]] | +0.58 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[MTERF2]] | +0.58 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[HPS1]] | +0.58 | +0.62 / +0.26 | both halves | 4e-04 |  |
| [[SPART-AS1]] | +0.58 | +0.49 / +0.28 | both halves | 3e-04 |  |
| [[PHYH]] | +0.57 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[TTC33]] | +0.57 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[DAZAP2]] | +0.56 | +0.42 / +0.34 | both halves | 1e-04 |  |
| [[CAMK2D]] | +0.56 | +0.58 / +0.32 | both halves | 2e-04 |  |
| [[GNPDA1]] | +0.56 | +0.56 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND19]] | -0.62 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[NUP93]] | -0.60 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[WDR5]] | -0.60 | -0.73 / -0.30 | both halves | 2e-04 |  |
| [[WRN]] | -0.59 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[SRM]] | -0.57 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[TREX2]] | -0.56 | -0.62 / -0.32 | both halves | 1e-04 |  |
| [[RBM6]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ATAD3B]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CTU2]] | -0.56 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[VKORC1L1]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[GNB1L]] | -0.54 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[PINX1-1]] | -0.54 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN5]] | B | HMGN5 activity raises SNX16's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without HMGN5 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction -0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, -8.3); signed map (17.4, -14.8). **Vector** length 76.2, 13.6% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +23.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.2 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +5.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.1 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:81,799,581-81,842,866 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [P57768](https://www.uniprot.org/uniprotkb/P57768) (Sorting nexin-16):

> May be involved in several stages of intracellular trafficking. Plays a role in protein transport from early to late endosomes. Plays a role in protein transport to the lysosome. Promotes degradation of EGFR after EGF signaling. Plays a role in intracellular transport of vesicular stomatitis virus nucleocapsids from the endosome to the cytoplasm.

**Summary**, from NCBI Gene [64089](https://www.ncbi.nlm.nih.gov/gene/64089):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. The protein encoded by this gene associates with late endosome membranes as is involved in tubule formation, cholesterol transport, and transport of tetraspanin CD81. The encoded protein also inhibits cell migration and tumorigenesis. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:14980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14980) · Entrez [64089](https://www.ncbi.nlm.nih.gov/gene/64089) · UniProt [P57768](https://www.uniprot.org/uniprotkb/P57768) · Ensembl [ENSG00000104497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104497)

## Data

Gene col 2467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2467); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2467]; `tensor/DDL_lfc|DDL_z.npy` [2467]; `embed/gene_vectors.npy` [2467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2467 or target_col == 2467). Every well: [[SNX16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

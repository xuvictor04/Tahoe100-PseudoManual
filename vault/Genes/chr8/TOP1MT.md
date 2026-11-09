---
symbol: "TOP1MT"
type: "gene"
col: 11534
ensembl_id: "ENSG00000184428"
name: "DNA topoisomerase I mitochondrial"
location: "8q24.3"
module: 18
arm: "+"
pooled_cpm: 19.14
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TOP1MT

*DNA topoisomerase I mitochondrial* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.40× (z +16.5, q 0e+00, up in 27 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sapanisertib (drug)]] 0.05 µM: 1.29× (z +4.7, q 3e-04, up in 9 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.710× (z -6.5, q 5e-08, down in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.731× (z -6.2, q 2e-07, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEH1L]] (+0.63, fdr 9e-06), [[CPNE7]] (+0.63, fdr 7e-06), [[RPSA]] (+0.61, fdr 1e-05); moves opposite to [[CDKN2C]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +16.5 | 0e+00 | 27/31 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +14.8 | 0e+00 | 35/42 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +10.6 | 4e-24 | 30/38 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.7 | 1e-06 | 18/47 (NCI-H1792, HT-29, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.29×** | +4.7 | 3e-04 | 9/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +4.6 | 3e-04 | 14/43 (KATO III, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +4.4 | 7e-04 | 15/46 (HEC-1-A, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.3 | 0.001 | 8/48 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 10/47 (NCI-H2030, SW1417, …) | inconsistent across doses | position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.004 | 4/47 (CHP-212, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.21×** | +3.7 | 0.010 | 11/47 (SW1417, SNU-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.21×** | +3.7 | 0.010 | 11/47 (HT-29, KATO III, …) | two highest doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.010 | 13/47 (NCI-H1792, J82, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.5 | 0.020 | 5/48 (NCI-H2030, HT-29, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.025 | 11/47 (KATO III, A-427, …) | two highest doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.026 | 11/47 (HepG2/C3A, NCI-H1792, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.047 | 4/48 (SW1417, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.077 | 5/45 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.710×** | -6.5 | 5e-08 | 24/47 (PANC-1, NCI-H23, …) | top dose only | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.731×** | -6.2 | 2e-07 | 20/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.746×** | -5.8 | 1e-06 | 22/48 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.814×** | -5.8 | 1e-06 | 26/47 (Panc 03.27, A-427, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.753×** | -5.6 | 2e-06 | 20/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.785×** | -4.8 | 2e-04 | 20/46 (NCI-H661, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.788×** | -4.7 | 2e-04 | 13/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.7 | 2e-04 | 15/48 (LOX-IMVI, NCI-H460, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -4.5 | 4e-04 | 15/48 (NCI-H2030, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.666×** | -4.2 | 0.002 | 16/48 (RKO, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.806×** | -4.1 | 0.002 | 14/46 (CHP-212, C-33 A, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.820×** | -3.9 | 0.004 | 16/47 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.694×** | -3.8 | 0.007 | 14/45 (COLO 205, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.011 | 17/46 (A549, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.890× | -3.3 | 0.043 | 5/48 (NCI-H23, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.839× | -3.2 | 0.047 | 6/47 (COLO 205, C-33 A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.875× | -3.0 | 0.083 | 4/48 (HCT15, BT-474, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 17.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +12.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 21.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -11.1) |
| [[SW480 (line)]] | alt | 21.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A498 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +8.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.123× (z -11.0) |
| [[COLO 205 (line)]] | alt | 8.43 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0950× (z -8.7) |
| [[H4 (line)]] | wt | 10.4 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0800× (z -9.6) |
| [[HOP62 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.40× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 20.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.7) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H1792 (line)]] | alt | 8.85 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +13.9) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H23 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.330× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SHP-77 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.2) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEH1L]] | +0.63 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[CPNE7]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RPSA]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[AHCY]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[HEATR1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MTA1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RPS18]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[EIF3C]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[RPS3A]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NOC2L]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DDX54]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SMG1P3]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2C]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises TOP1MT's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without SLC4A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[GARNL3]] | C | GARNL3 activity raises TOP1MT's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without GARNL3 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-25.4, -38.6); signed map (-1.9, -55.2). **Vector** length 85.7, 16.3% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +10.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.4 | -6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.4 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.6 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | DNA topoisomerase I mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,304,384-143,359,979 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Topoisomerases; Mitochondrial nucleoid associated proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969P6](https://www.uniprot.org/uniprotkb/Q969P6) (DNA topoisomerase I, mitochondrial):

> Releases the supercoiling and torsional tension of DNA introduced during duplication of mitochondrial DNA by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(3'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 5'-OH DNA strand. The free DNA strand then rotates …

**Summary**, from NCBI Gene [116447](https://www.ncbi.nlm.nih.gov/gene/116447):

> This gene encodes a mitochondrial DNA topoisomerase that plays a role in the modification of DNA topology. The encoded protein is a type IB topoisomerase and catalyzes the transient breaking and rejoining of DNA to relieve tension and DNA supercoiling generated in the mitochondrial genome during replication and transcription. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:29787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29787) · Entrez [116447](https://www.ncbi.nlm.nih.gov/gene/116447) · UniProt [Q969P6](https://www.uniprot.org/uniprotkb/Q969P6) · Ensembl [ENSG00000184428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184428)

## Data

Gene col 11534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11534); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11534]; `tensor/DDL_lfc|DDL_z.npy` [11534]; `embed/gene_vectors.npy` [11534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11534 or target_col == 11534). Every well: [[TOP1MT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOP1MT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

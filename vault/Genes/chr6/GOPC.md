---
symbol: "GOPC"
type: "gene"
col: 526
ensembl_id: "ENSG00000047932"
name: "golgi associated PDZ and coiled-coil motif containing"
location: "6q22.1"
module: 16
arm: "+"
pooled_cpm: 45.89
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 26
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# GOPC

*golgi associated PDZ and coiled-coil motif containing* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +18.0, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.713× (z -5.6, q 1e-05, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM4]] (+0.69, fdr 7e-06), [[AASDHPPT]] (+0.69, fdr 7e-06), [[ZNF480]] (+0.67, fdr 7e-06); moves opposite to [[KLHL25]] (-0.66, fdr 1e-05), [[BUD23]] (-0.62, fdr 3e-05), [[DNAJC5]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +18.0 | 0e+00 | 40/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +14.2 | 4e-43 | 42/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +9.1 | 1e-17 | 34/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.8 | 6e-13 | 33/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +6.8 | 8e-10 | 32/47 (A-172, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +6.7 | 2e-09 | 32/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.5 | 5e-09 | 33/48 (AsPC-1, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.2 | 4e-08 | 32/48 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +5.7 | 1e-06 | 31/48 (A-172, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +5.6 | 1e-06 | 29/49 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +5.6 | 1e-06 | 26/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 6e-06 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 1e-05 | 28/47 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.34×** | +4.8 | 8e-05 | 29/48 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 22/48 (A-172, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -5.6 | 1e-05 | 28/48 (HCT15, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 1e-04 | 25/48 (SW 1088, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.738×** | -4.8 | 2e-04 | 20/40 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -4.8 | 2e-04 | 25/48 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.769×** | -4.4 | 0.002 | 25/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.6 | 0.028 | 16/48 (A-427, CHP-212, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **0.822×** | -3.3 | 0.091 | 17/48 (BT-474, SNU-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.695× | -3.2 | 0.10 | 19/48 (SK-MEL-2, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.814× | -3.2 | 0.10 | 15/47 (COLO 205, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 56.8 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +25.1) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 84.2 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +31.5) | [[Digitoxin (drug)]] 5 µM 0.395× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.436× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 19.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +29.8) | — |
| [[SW48 (line)]] | wt | 37.3 | 3 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 9.12× (z +12.2) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0565× (z -16.7) |
| [[A498 (line)]] | wt | 54.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +24.5) | — |
| [[H4 (line)]] | wt | 35.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +16.1) | — |
| [[HS-578T (line)]] | alt | 39.5 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 10.6× (z +17.2) | — |
| [[KATO III (line)]] | alt | 62.1 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.6 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 16.6× (z +18.9) | — |
| [[SW480 (line)]] | alt | 78.4 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.09× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 34.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +19.3) | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +27.5) | — |
| [[hTERT-HPNE (line)]] | wt | 49.6 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 9.12× (z +14.9) | — |
| [[J82 (line)]] | alt | 33.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +27.4) | — |
| [[A-427 (line)]] | wt | 38.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 44.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 44.1 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.32× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 38.5 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.128× (z -9.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.19× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 35.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.341× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 29.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +19.5) | — |
| [[SK-MEL-2 (line)]] | alt | 34.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +17.8) | — |
| [[SNU-423 (line)]] | alt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +16.4) | — |
| [[BT-474 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -12.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 50.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.9) | — |
| [[LoVo (line)]] | wt | 43.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.28× (z +12.6) | — |
| [[NCI-H661 (line)]] | alt | 41.9 | 0 | 1 | — | [[Proglumide (drug)]] 0.5 µM 0.0682× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 43.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.19× (z +13.7) | — |
| [[AN3 CA (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.69 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[REPIN1]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.67 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RAD50]] | +0.65 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[UBQLN2]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[USP40]] | +0.65 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[ZNF776]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.64 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL25]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[BUD23]] | -0.62 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[DNAJC5]] | -0.61 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[INPP5A]] | -0.61 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[MFN1]] | -0.60 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[ASB16-AS1]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SS18L1]] | -0.57 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[HDAC3]] | -0.57 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[UBA6]] | -0.56 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[ISCA1]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[TENT4A]] | -0.56 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[SCAI]] | -0.56 | -0.67 / -0.45 | both halves | 3e-05 | pathway: RHO GTPase Effectors |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers GOPC's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.9, 11.0); signed map (4.3, -28.2). **Vector** length 112, 30.6% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.1 | +14.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.1 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.3 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +18.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.2 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | golgi associated PDZ and coiled-coil motif containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:117,560,269-117,602,542 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ94G16.2, PIST, FIG, GOPC1, CAL |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 6 pathways, smallest: RHO GTPases regulate CFTR trafficking; RHOQ GTPase cycle; RHO GTPase Effectors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD26](https://www.uniprot.org/uniprotkb/Q9HD26) (Golgi-associated PDZ and coiled-coil motif-containing protein):

> Plays a role in intracellular protein trafficking and degradation. May regulate CFTR chloride currents and acid-induced ASIC3 currents by modulating cell surface expression of both channels (By similarity). May also regulate the intracellular trafficking of the ADR1B receptor. May play a role in autophagy (By similarity). Together with MARCHF2 mediates the ubiquitination and lysosomal degradation of CFTR. Overexpression results in CFTR intracellular retention and lysosomaldegradation in the …

**Summary**, from NCBI Gene [57120](https://www.ncbi.nlm.nih.gov/gene/57120):

> This gene encodes a Golgi protein with a PDZ domain. The PDZ domain is globular and proteins which contain them bind other proteins through short motifs near the C-termini. Mice which are deficient in the orthologous protein have globozoospermia and are infertile. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:17643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17643) · Entrez [57120](https://www.ncbi.nlm.nih.gov/gene/57120) · UniProt [Q9HD26](https://www.uniprot.org/uniprotkb/Q9HD26) · Ensembl [ENSG00000047932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047932)

## Data

Gene col 526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 526); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 526]; `tensor/DDL_lfc|DDL_z.npy` [526]; `embed/gene_vectors.npy` [526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 526 or target_col == 526). Every well: [[GOPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOPC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

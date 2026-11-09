---
symbol: "AUP1"
type: "gene"
col: 3656
ensembl_id: "ENSG00000115307"
name: "AUP1 lipid droplet regulating VLDL assembly factor"
location: "2p13.1"
module: 7
arm: "+"
pooled_cpm: 35.71
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# AUP1

*AUP1 lipid droplet regulating VLDL assembly factor* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +13.9, q 2e-41, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.05× (z +8.7, q 7e-16, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN29]] (+0.71, fdr 7e-06), [[SBDSP1-1]] (+0.68, fdr 1e-05), [[ACTR8]] (+0.66, fdr 1e-05); moves opposite to [[SBNO1]] (-0.58, fdr 3e-05), [[PTMA]] (-0.55, fdr 6e-05), [[COX6A1]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRIP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +13.9 | 2e-41 | 45/45 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.1 | 3e-31 | 33/38 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +8.7 | 7e-16 | 44/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.2 | 3e-14 | 45/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.69×** | +6.6 | 5e-09 | 37/46 (A-427, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.5 | 8e-09 | 34/41 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.6 | 1e-06 | 32/46 (C32, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +5.5 | 3e-06 | 35/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.47×** | +4.7 | 2e-04 | 30/47 (C32, C-33 A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 4e-04 | 32/47 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.4 | 6e-04 | 27/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.003 | 22/48 (NCI-H23, A-427, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +3.7 | 0.011 | 23/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.32×** | +3.5 | 0.017 | 22/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.017 | 19/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.018 | 17/48 (C32, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.024 | 21/48 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.66×** | +3.3 | 0.024 | 15/48 (MIA PaCa-2, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.028 | 14/48 (HT-29, NCI-H460, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.040 | 18/48 (HOP62, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.059 | 15/48 (LoVo, KATO III, …) | inconsistent across doses | position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.067 | 16/48 (KATO III, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 71.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +12.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 23.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 29.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 55.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 27.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.98× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN29]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SBDSP1-1]] | +0.68 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[ACTR8]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[WIZ]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[GFER]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[EIF2B5]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[ERAL1]] | +0.63 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[ZXDB]] | +0.63 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[ZNF543]] | +0.61 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[BRPF3]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DXO]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBNO1]] | -0.58 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[PTMA]] | -0.55 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[COX6A1]] | -0.55 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[IGFBP2]] | -0.54 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[SEPTIN6]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[LPCAT2]] | -0.53 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ABCB9]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[FBXO33]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[FAM13B]] | -0.52 | -0.51 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity lowers AUP1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.17× higher at baseline in the lines without TRIP6 | 0.097 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-27.2, 9.2); signed map (11.5, -22.2). **Vector** length 58.6, 12.2% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | +0.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | +1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -0.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | AUP1 lipid droplet regulating VLDL assembly factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,526,645-74,529,760 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CUE domain containing |
| Reactome | 3 pathways, smallest: Dengue Virus-Host Interactions; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y679](https://www.uniprot.org/uniprotkb/Q9Y679) (Lipid droplet-regulating VLDL assembly factor AUP1):

> Plays a role in the translocation of terminally misfolded proteins from the endoplasmic reticulum lumen to the cytoplasm and their degradation by the proteasome. Plays a role in lipid droplet formation. Induces lipid droplet clustering. Recruits ubiquitin-conjugating enzyme UBE2G2 to lipid droplets which facilitates its interaction with ubiquitin ligases AMFR/gp78 and RNF139/TRC8, leading to sterol-induced ubiquitination of HMGCR and its subsequent proteasomal degradation. Also required for the …

**Summary**, from NCBI Gene [550](https://www.ncbi.nlm.nih.gov/gene/550):

> The protein encoded this gene is involved in several pathways including quality control of misfolded proteins in the endoplasmic reticulum and lipid droplet accumulation. Lipid droplets are organelles in the cytoplasm that store neutral lipids such as cholesterol esters and trigylycerides to prevent the overabundance of free cholesterol and fatty acids in cells, but also to act as storage for other metabolic processes, such as membrane biogenesis. Reduced expression of this gene results in …

**Accessions** — [HGNC:891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:891) · Entrez [550](https://www.ncbi.nlm.nih.gov/gene/550) · UniProt [Q9Y679](https://www.uniprot.org/uniprotkb/Q9Y679) · Ensembl [ENSG00000115307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115307)

## Data

Gene col 3656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3656); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3656]; `tensor/DDL_lfc|DDL_z.npy` [3656]; `embed/gene_vectors.npy` [3656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3656 or target_col == 3656). Every well: [[AUP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AUP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

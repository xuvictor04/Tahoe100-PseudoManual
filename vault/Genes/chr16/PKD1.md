---
symbol: "PKD1"
type: "gene"
col: 178
ensembl_id: "ENSG00000008710"
name: "polycystin 1, transient receptor potential channel interacting"
location: "16p13.3"
module: 3
arm: "+"
pooled_cpm: 29.87
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PKD1

*polycystin 1, transient receptor potential channel interacting* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.03× (z +11.7, q 9e-29, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.389× (z -14.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKD1P6]] (+0.87, fdr 7e-06), [[STK32C]] (+0.71, fdr 7e-06), [[SLC26A6]] (+0.67, fdr 1e-05); moves opposite to [[DECR1]] (-0.59, fdr 4e-05), [[MTMR2]] (-0.56, fdr 4e-05), [[TFAM]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +11.7 | 9e-29 | 42/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +8.3 | 2e-14 | 36/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +7.7 | 3e-12 | 33/48 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.2 | 0.005 | 18/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.065 | 10/48 (NCI-H1573, Hs 766T, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.15× | +3.3 | 0.091 | 14/48 (SW48, SNU-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.22× | +3.2 | 0.11 | 12/47 (A-172, LoVo, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.21× | +3.1 | 0.14 | 4/48 (AsPC-1, BT-474, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.14 | 14/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.389×** | -14.9 | 0e+00 | 45/48 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.293×** | -10.5 | 2e-23 | 43/48 (Hs 766T, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -10.2 | 3e-22 | 29/37 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.582×** | -8.9 | 1e-16 | 31/44 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.462×** | -8.3 | 1e-14 | 31/39 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.607×** | -8.2 | 2e-14 | 34/48 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.513×** | -5.7 | 9e-07 | 27/47 (hTERT-HPNE, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -5.6 | 1e-06 | 27/45 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -4.4 | 8e-04 | 22/48 (A-172, SNU-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.792×** | -3.8 | 0.008 | 19/47 (A-427, A-172, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.797×** | -3.7 | 0.011 | 17/48 (SW 1271, HCT15, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | 0.823× | -3.1 | 0.11 | 15/47 (SNU-423, SNU-1, …) | top dose only | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.878× | -3.0 | 0.11 | 14/48 (PANC-1, SW 1271, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 63.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.215× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 20.2 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.62× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0880× (z -20.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.285× (z -9.9) |
| [[KATO III (line)]] | alt | 35.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0732× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.299× (z -8.7) |
| [[LoVo (line)]] | wt | 25.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.81× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.300× (z -9.6) |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.211× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 28.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -14.2) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A498 (line)]] | wt | 31.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.405× (z -8.5) |
| [[AN3 CA (line)]] | alt | 36.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.109× (z -9.2) |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -10.1) |
| [[Hs 766T (line)]] | wt | 33.0 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.05× (z +8.5) | [[TAK-901 (drug)]] 5 µM 0.0744× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 45.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.310× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.290× (z -9.3) |
| [[PANC-1 (line)]] | alt | 47.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.422× (z -9.2) ⚠ cell-cycle shift, explains ~19% of this change |
| [[RPMI-7951 (line)]] | alt | 64.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.251× (z -11.2) |
| [[SW1417 (line)]] | alt | 25.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +9.5) | — |
| [[SW480 (line)]] | alt | 22.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -10.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 17.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.337× (z -9.3) |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -10.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0656× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.249× (z -8.9) |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0681× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD1P6]] | +0.87 | +0.83 / +0.84 | both halves | 7e-06 |  |
| [[STK32C]] | +0.71 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[SLC26A6]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 | same gene group |
| [[MKNK2]] | +0.66 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[GIT1]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CDC34]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MPND]] | +0.64 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ENO2]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KDM4B]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.63 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PRSS53]] | +0.62 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[MIGA2]] | +0.62 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.59 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MTMR2]] | -0.56 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TFAM]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[ZC3H12C]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[AASDHPPT]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CASC9]] | -0.54 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ACADM]] | -0.54 | -0.37 / -0.50 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PKD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDGFRA]] | B | PDGFRA activity lowers PKD1's level | compounds that target PDGFRA: 2 of 3 raise it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[SOX12]] | B | SOX12 activity raises PKD1's level | lines that do not express SOX12 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without SOX12 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENAH, ACOT12, SSBP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.4, -3.2); signed map (-31.5, 18.1). **Vector** length 113, 29.1% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +11.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +8.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.3 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -14.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.1 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.2 | -8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -5.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | polycystin 1, transient receptor potential channel interacting |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,088,708-2,135,898 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PBP, Pc-1, TRPP1 |
| Gene groups (HGNC) | C-type lectin domain containing; MicroRNA protein coding host genes |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: VxPx cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P98161](https://www.uniprot.org/uniprotkb/P98161) (Polycystin-1):

> Component of a heteromeric calcium-permeable ion channel formed by PKD1 and PKD2 that is activated by interaction between PKD1 and a Wnt family member, such as WNT3A and WNT9B. Both PKD1 and PKD2 are required for channel activity. Involved in renal tubulogenesis. Involved in fluid-flow mechanosensation by the primary cilium in renal epithelium (By similarity). Acts as a regulator of cilium length, together with PKD2 (By similarity). The dynamic control of cilium length is essential in the …

**Summary**, from NCBI Gene [5310](https://www.ncbi.nlm.nih.gov/gene/5310):

> This gene encodes a member of the polycystin protein family. The encoded glycoprotein contains a large N-terminal extracellular region, multiple transmembrane domains and a cytoplasmic C-tail. It is an integral membrane protein that functions as a regulator of calcium permeable cation channels and intracellular calcium homoeostasis. It is also involved in cell-cell/matrix interactions and may modulate G-protein-coupled signal-transduction pathways. It plays a role in renal tubular development, …

**Accessions** — [HGNC:9008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9008) · Entrez [5310](https://www.ncbi.nlm.nih.gov/gene/5310) · UniProt [P98161](https://www.uniprot.org/uniprotkb/P98161) · Ensembl [ENSG00000008710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008710)

## Data

Gene col 178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 178); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 178]; `tensor/DDL_lfc|DDL_z.npy` [178]; `embed/gene_vectors.npy` [178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 178 or target_col == 178). Every well: [[PKD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

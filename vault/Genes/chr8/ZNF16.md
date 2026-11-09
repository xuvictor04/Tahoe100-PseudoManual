---
symbol: "ZNF16"
type: "gene"
col: 9987
ensembl_id: "ENSG00000170631"
name: "zinc finger protein 16"
location: "8q24.3"
module: 107
arm: "+"
pooled_cpm: 16.75
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# ZNF16

*zinc finger protein 16* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 8.10× (z +15.8, q 0e+00, up in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 15.5×, RKO 20.5×, HEC-1-A 12.7×, NCI-H23 9.45×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW480 12.2×, RKO 14.7×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.482× (z -10.1, q 2e-21, down in 24 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.545× (z -8.4, q 5e-15, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF322]] (+0.76, fdr 7e-06), [[ZNF3]] (+0.73, fdr 7e-06), [[WDR53]] (+0.73, fdr 7e-06); moves opposite to [[PEAK1]] (-0.60, fdr 1e-05), [[GLS]] (-0.58, fdr 1e-05), [[BAIAP2]] (-0.57, fdr 1e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 15.5×, RKO 20.5×, HEC-1-A 12.7×, NCI-H23 9.45×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW480 12.2×, RKO 14.7×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.10×** | +15.8 | 0e+00 | 44/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.05×** | +12.2 | 6e-32 | 37/44 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Oxaliplatin (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.35 | 7/48 (NCI-H2347, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.482×** | -10.1 | 2e-21 | 24/30 (PANC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.493×** | -9.8 | 2e-20 | 31/43 (SNU-1, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.512×** | -9.7 | 8e-20 | 32/42 (HS-578T, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -8.4 | 5e-15 | 30/46 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.535×** | -8.4 | 7e-15 | 24/32 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.581×** | -7.8 | 4e-13 | 35/48 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -7.3 | 3e-11 | 29/47 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.622×** | -6.9 | 5e-10 | 31/47 (J82, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.658×** | -6.0 | 1e-07 | 25/47 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.671×** | -5.8 | 4e-07 | 24/47 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -5.6 | 9e-07 | 24/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.695×** | -5.3 | 7e-06 | 23/48 (NCI-H460, LoVo, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -4.9 | 4e-05 | 22/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.789×** | -4.8 | 5e-05 | 23/47 (HS-578T, AsPC-1, …) | top dose only | composition shift |
| [[Gefitinib (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.002 | 13/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.013 | 9/47 (SW 1271, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -3.4 | 0.018 | 13/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.797×** | -3.3 | 0.031 | 11/48 (NCI-H661, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.863× | -3.0 | 0.074 | 12/48 (A-172, HOP62, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.806×** | -2.9 | 0.087 | 13/47 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -12.0) |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.259× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 27.4 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.45× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -14.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -12.5) |
| [[SW480 (line)]] | alt | 15.2 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.5× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.4 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0711× (z -15.8) |
| [[J82 (line)]] | alt | 16.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.218× (z -9.4) ⚠ toxic |
| [[RKO (line)]] | wt | 33.8 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 20.5× (z +11.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.1) |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -12.0) |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0789× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Canagliflozin (drug)]] 5 µM 0.151× (z -8.7) |
| [[A-427 (line)]] | wt | 27.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.313× (z -8.8) |
| [[A498 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0931× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HEC-1-A (line)]] | alt | 13.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.7× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 9.40 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0851× (z -9.2) |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.179× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 9.62 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.106× (z -9.1) |
| [[KATO III (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.136× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -10.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0659× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF322]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | same gene group |
| [[ZNF3]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 | same gene group |
| [[WDR53]] | +0.73 | +0.64 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ZNF777]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 | same gene group |
| [[ZNF329]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 | same gene group |
| [[DHX57]] | +0.69 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[ZNF35]] | +0.69 | +0.53 / +0.70 | both halves | 1e-05 | same gene group |
| [[ALKBH1]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ZNF282]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 | same gene group |
| [[GTF3C2]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ZNF865]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 | same gene group |
| [[RPUSD2]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[GLS]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[BAIAP2]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | ZNF16's natural level raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (protects the cells) | ZNF16's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.287 over the table, 0.080 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.6, 4.6); signed map (-10.8, -15.3). **Vector** length 97.9, 22.3% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.2 | +15.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.6 | +12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +2.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.3 | -9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.1 | -9.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.3 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,930,358-144,950,888 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX9 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P17020](https://www.uniprot.org/uniprotkb/P17020) (Zinc finger protein 16):

> Acts as a transcriptional activator. Promotes cell proliferation by facilitating the cell cycle phase transition from the S to G2/M phase. Involved in both the hemin- and phorbol myristate acetate (PMA)-induced erythroid and megakaryocytic differentiation, respectively. Also plays a role as an inhibitor of cell apoptosis.

**Summary**, from NCBI Gene [7564](https://www.ncbi.nlm.nih.gov/gene/7564):

> The protein encoded by this gene contains multiple tandem zinc finger motifs. The encoded protein is involved in the differentiation of erythroid and megakaryocytic cells. This gene is located in a cluster of related genes on chromosome 8 encoding zinc finger proteins. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:12947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12947) · Entrez [7564](https://www.ncbi.nlm.nih.gov/gene/7564) · UniProt [P17020](https://www.uniprot.org/uniprotkb/P17020) · Ensembl [ENSG00000170631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170631)

## Data

Gene col 9987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9987); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9987]; `tensor/DDL_lfc|DDL_z.npy` [9987]; `embed/gene_vectors.npy` [9987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9987 or target_col == 9987). Every well: [[ZNF16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

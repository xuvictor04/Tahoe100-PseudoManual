---
symbol: "PROCR"
type: "gene"
col: 2057
ensembl_id: "ENSG00000101000"
name: "protein C receptor"
location: "20q11.22"
module: 12
arm: "-"
pooled_cpm: 18.02
n_lines_expressing: 42
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PROCR

*protein C receptor* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.62× (z +14.2, q 4e-43, up in 19 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +10.1, q 1e-21, up in 22 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -12.8, q 1e-34, down in 32 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXYD5]] (+0.63, fdr 1e-05), [[LAPTM4B]] (+0.58, fdr 1e-05), [[ECM1]] (+0.57, fdr 1e-05); moves opposite to [[XRCC1]] (-0.60, fdr 8e-06), [[CHMP4A]] (-0.55, fdr 3e-05), [[LGALS3]] (-0.54, fdr 6e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[ADAT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.62×** | +14.2 | 4e-43 | 19/20 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.98×** | +12.5 | 1e-33 | 27/31 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +10.1 | 1e-21 | 22/38 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +9.6 | 2e-19 | 30/34 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.20×** | +8.4 | 6e-15 | 18/26 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.0 | 2e-10 | 28/39 (Hs 766T, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.7 | 2e-04 | 19/39 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 3e-04 | 21/37 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.48×** | +4.5 | 4e-04 | 20/38 (A549, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.005 | 12/38 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.41×** | +3.8 | 0.009 | 14/38 (A549, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 15/38 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.7 | 0.010 | 13/36 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +3.6 | 0.015 | 15/38 (A498, Hs 766T, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.35×** | +3.5 | 0.020 | 10/37 (NCI-H460, KATO III, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.66×** | +3.0 | 0.072 | 10/35 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.456×** | -12.8 | 1e-34 | 32/37 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -8.1 | 1e-13 | 29/37 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -7.6 | 6e-12 | 28/38 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.737× | -3.0 | 0.28 | 11/40 (Hs 766T, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.2 | 4 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -11.9) |
| [[A549 (line)]] | wt | 43.8 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 32.4 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.1) |
| [[HT-29 (line)]] | alt | 15.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.0) |
| [[PANC-1 (line)]] | alt | 43.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -24.4) |
| [[RKO (line)]] | wt | 95.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -22.3) |
| [[CFPAC-1 (line)]] | alt | 13.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.34× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.5) |
| [[A-172 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -18.2) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -12.2) |
| [[Hs 766T (line)]] | wt | 91.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.8) |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 7.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -10.7) |
| [[SW48 (line)]] | wt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.5) |
| [[A-427 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXYD5]] | +0.63 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[LAPTM4B]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ECM1]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[USB1]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[EGFL7]] | +0.55 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[GPX3]] | +0.54 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[SDC1]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 | same gene group; pathway: HALLMARK_P53_PATHWAY |
| [[AP1S1]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[HAGLR]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[PIGF]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CPSF4]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC1]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[CHMP4A]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[LGALS3]] | -0.54 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[PPIG]] | -0.53 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[DNAL4]] | -0.53 | -0.61 / -0.37 | both halves | 9e-05 |  |
| [[DARS1]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[EMC9]] | -0.52 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[CIRBP]] | -0.52 | -0.59 / -0.37 | both halves | 7e-05 |  |
| [[NBR1]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[MKS1]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RNF214]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[CEP350]] | -0.51 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAT2]] | B | PROCR activity lowers ADAT2's level | lines that do not express PROCR (8) vs lines expressing it (42) | 1.94× higher at baseline in the lines without PROCR | 0.058 | ⚠ within organs, on part of the lines; also absent: ATP2B4, RNF135, LAMB1; maybe low, not absent |
| [[FXYD5]] | B | PROCR activity raises FXYD5's level | lines that do not express PROCR (8) vs lines expressing it (42) | 2.80× lower at baseline in the lines without PROCR | 0.059 | ⚠ within organs, on part of the lines; also absent: ATP2B4, RNF135, LAMB1; maybe low, not absent |
| [[ANKRD13B]] | B | PROCR activity lowers ANKRD13B's level | lines that do not express PROCR (8) vs lines expressing it (42) | 1.50× higher at baseline in the lines without PROCR | 0.097 | ⚠ within organs, on part of the lines; also absent: ATP2B4, RNF135, LAMB1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.416). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.7, -13.1); signed map (-53.5, -12.5). **Vector** length 72.7, 15.6% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.0 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.8 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.8 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.2 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein C receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,172,072-35,216,240 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPCR, CCD41, CD201 |
| Gene groups (HGNC) | CD molecules |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, P53_PATHWAY |
| Reactome | 4 pathways, smallest: Regulation of clotting cascade; Coagulation pathway; Cell surface interactions at the vascular wall |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNN8](https://www.uniprot.org/uniprotkb/Q9UNN8) (Endothelial protein C receptor):

> Binds activated protein C. Enhances protein C activation by the thrombin-thrombomodulin complex; plays a role in the protein C pathway controlling blood coagulation.

**Summary**, from NCBI Gene [10544](https://www.ncbi.nlm.nih.gov/gene/10544):

> The protein encoded by this gene is a receptor for activated protein C, a serine protease activated by and involved in the blood coagulation pathway. The encoded protein is an N-glycosylated type I membrane protein that enhances the activation of protein C. Mutations in this gene have been associated with venous thromboembolism and myocardial infarction, as well as with late fetal loss during pregnancy. The encoded protein may also play a role in malarial infection and has been associated with …

**Accessions** — [HGNC:9452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9452) · Entrez [10544](https://www.ncbi.nlm.nih.gov/gene/10544) · UniProt [Q9UNN8](https://www.uniprot.org/uniprotkb/Q9UNN8) · Ensembl [ENSG00000101000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101000)

## Data

Gene col 2057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2057); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2057]; `tensor/DDL_lfc|DDL_z.npy` [2057]; `embed/gene_vectors.npy` [2057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2057 or target_col == 2057). Every well: [[PROCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ZKSCAN2"
type: "gene"
col: 7905
ensembl_id: "ENSG00000155592"
name: "zinc finger with KRAB and SCAN domains 2"
location: "16p12.1"
module: 16
arm: "+"
pooled_cpm: 8.04
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZKSCAN2

*zinc finger with KRAB and SCAN domains 2* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +12.9, q 3e-35, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.663× (z -5.1, q 2e-04, down in 17 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.807× (z -3.8, q 0.029, down in 14 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.154×, HOP62 0.148×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (Hs 766T 0.0733×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.167×); [[Mozavaptan (drug)]] 5 µM in 1 line (A-172 0.0759×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM185B]] (+0.74, fdr 7e-06), [[CSTF2T]] (+0.72, fdr 7e-06), [[RTL6]] (+0.70, fdr 7e-06); moves opposite to [[SRP54-AS1]] (-0.67, fdr 7e-06), [[MAX]] (-0.67, fdr 7e-06), [[PIK3C2A]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GDAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +12.9 | 3e-35 | 38/42 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +10.9 | 3e-25 | 32/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +9.2 | 1e-17 | 34/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.97×** | +8.9 | 7e-17 | 36/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.1 | 8e-14 | 29/41 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +7.3 | 4e-11 | 29/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +7.2 | 4e-11 | 27/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +6.7 | 1e-09 | 25/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.6 | 1e-06 | 22/45 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.8 | 1e-04 | 14/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +4.7 | 1e-04 | 13/47 (HOP62, HS-578T, …) | top dose only | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.4 | 5e-04 | 14/47 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.1 | 0.002 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.003 | 14/44 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.3 | 0.038 | 4/47 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7905.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H23 0.154×, HOP62 0.148×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (Hs 766T 0.0733×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.167×); [[Mozavaptan (drug)]] 5 µM in 1 line (A-172 0.0759×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.663×** | -5.1 | 2e-04 | 17/33 (HS-578T, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -4.5 | 0.002 | 19/39 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.8 | 0.029 | 14/44 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.029 | 20/46 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.20 | 0 | 2 (1 ⚠) | — | [[Mozavaptan (drug)]] 5 µM 0.0759× (z -10.0) |
| [[HT-29 (line)]] | alt | 4.24 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0730× (z -9.2) |
| [[SW480 (line)]] | alt | 7.71 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 5.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 6.66 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0553× (z -9.6) |
| [[COLO 205 (line)]] | alt | 5.18 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.05 µM 0.0499× (z -9.4) |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0771× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 9.38 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -10.2) |
| [[HOP62 (line)]] | alt | 5.87 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.148× (z -9.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0733× (z -10.2) |
| [[HS-578T (line)]] | alt | 5.77 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0815× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.135× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -10.1) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 4.92 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0704× (z -9.3) |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 6.02 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.122× (z -8.9) |
| [[SW1417 (line)]] | alt | 5.63 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0828× (z -9.2) |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.72 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[RTL6]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.69 | +0.75 / +0.69 | both halves | 7e-06 | same gene group |
| [[PUF60]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ZNF414]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZNF502]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 | same gene group |
| [[ZNF510]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | same gene group |
| [[THUMPD3]] | +0.68 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ZFP41]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.67 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[MAX]] | -0.67 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[PIK3C2A]] | -0.67 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[APTR]] | -0.65 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[TMEM50B]] | -0.64 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[IFT20]] | -0.64 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[SGK3]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | -0.62 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[ABHD18]] | -0.61 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[SOS1]] | -0.61 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.61 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[FBXL20]] | -0.60 | -0.65 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDAP1]] | B | GDAP1 activity raises ZKSCAN2's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without GDAP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[ANAPC1P4]] | C | ANAPC1P4 activity raises ZKSCAN2's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without ANAPC1P4 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.6, 12.2); signed map (0.6, -30.7). **Vector** length 67.5, 10.3% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | -2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger with KRAB and SCAN domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:25,236,001-25,257,845 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23199, ZSCAN34; previously ZNF694 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; Myb/SANT domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q63HK3](https://www.uniprot.org/uniprotkb/Q63HK3) (Zinc finger protein with KRAB and SCAN domains 2):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [342357](https://www.ncbi.nlm.nih.gov/gene/342357):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25677) · Entrez [342357](https://www.ncbi.nlm.nih.gov/gene/342357) · UniProt [Q63HK3](https://www.uniprot.org/uniprotkb/Q63HK3) · Ensembl [ENSG00000155592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155592)

## Data

Gene col 7905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7905); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7905]; `tensor/DDL_lfc|DDL_z.npy` [7905]; `embed/gene_vectors.npy` [7905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7905 or target_col == 7905). Every well: [[ZKSCAN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZKSCAN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ANGEL1"
type: "gene"
col: 275
ensembl_id: "ENSG00000013523"
name: "angel homolog 1"
location: "14q24.3"
module: 1
arm: "+"
pooled_cpm: 10.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ANGEL1

*angel homolog 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.57× (z +6.6, q 2e-08, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.635× (z -6.7, q 1e-08, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB13]] (+0.78, fdr 7e-06), [[TMEM177]] (+0.67, fdr 7e-06), [[ZNHIT6]] (+0.66, fdr 7e-06); moves opposite to [[DNAI7]] (-0.58, fdr 3e-05), [[ZSWIM6]] (-0.52, fdr 2e-05), [[SLC7A9]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ADGRF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +6.6 | 2e-08 | 29/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +6.3 | 1e-07 | 22/47 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +6.2 | 1e-07 | 21/45 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.9 | 4e-07 | 20/40 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.6 | 3e-06 | 22/47 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.20× | +3.8 | 0.015 | 6/47 (NCI-H2347, SW48, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +3.7 | 0.018 | 11/47 (CFPAC-1, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.019 | 18/47 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.020 | 6/48 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.027 | 7/47 (HOP62, HCT15, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.027 | 8/46 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.052 | 4/47 (SW480, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -6.7 | 1e-08 | 24/47 (KATO III, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -4.6 | 9e-04 | 20/46 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.733×** | -4.6 | 9e-04 | 19/47 (SW480, SNU-1, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.577×** | -4.2 | 0.003 | 15/47 (NCI-H2030, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.751×** | -4.2 | 0.003 | 17/47 (SW48, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.805× | -3.2 | 0.12 | 12/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.797× | -3.2 | 0.12 | 9/45 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.808× | -3.0 | 0.17 | 9/48 (COLO 205, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 4.49 | 0 | 3 | — | [[Lumateperone (tosylate) (drug)]] 0.5 µM 0.0556× (z -10.6) |
| [[J82 (line)]] | alt | 4.97 | 0 | 2 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0926× (z -8.9) |
| [[SW480 (line)]] | alt | 19.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[A-427 (line)]] | wt | 15.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.226× (z -10.4) |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0586× (z -8.8) |
| [[BT-474 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 7.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0562× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 6.02 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0640× (z -11.2) |
| [[LS 180 (line)]] | wt | 6.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0777× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB13]] | +0.78 | +0.65 / +0.84 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ZNHIT6]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MIOS]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[PEX7]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[FARSA]] | +0.64 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[MECR]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MTFMT]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[DTD2]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI7]] | -0.58 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SLC7A9]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SKP1]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ALDH8A1]] | -0.50 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF4]] | B | ADGRF4 activity weakens ANGEL1's drug response | lines that do not express ADGRF4 (23) vs lines expressing it (24) | the lines without ADGRF4 respond 1.00× as strongly (z diff -0.21); strongest at Ixazomib citrate 5 µM: 0.57x vs 0.83x (z diff -2.2) | 0.005 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR; target measured in part of the lines; both ways; artifact flags |
| [[ADGRF4]] | B | ADGRF4 activity lowers ANGEL1's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 1.55× higher at baseline in the lines without ADGRF4 | 0.010 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[ATXN1]] | B | ATXN1 activity lowers ANGEL1's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.82× higher at baseline in the lines without ATXN1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[HDAC6]] | B | HDAC6 activity lowers ANGEL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NMNAT3]] | B | NMNAT3 activity raises ANGEL1's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without NMNAT3 | 0.098 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.6, -40.6); signed map (-7.3, -52.8). **Vector** length 70.8, 11.5% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +2.5 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.4 | +3.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | +1.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.2 | +1.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | angel homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:76,781,733-76,826,246 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ccr4e; previously KIAA0759 |
| Gene groups (HGNC) | Angel homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNK9](https://www.uniprot.org/uniprotkb/Q9UNK9) (RNA 2',3'-cyclic phosphatase ANGEL1):

> Exhibits weak RNA 2',3'-cyclic phosphatase, catalyzing the hydrolysis of RNA molecules with a 2',3'-cyclic phosphate at the 3' end to produce RNA with a linear 3'-phosphate group. Plays a role in the non-stop mRNA decay pathway (NSD), which specifically targets and degrades mRNAs that lack a proper stop codon.

**Summary**, from NCBI Gene [23357](https://www.ncbi.nlm.nih.gov/gene/23357):

> Enables RNA 2',3'-cyclic phosphatase activity; eukaryotic initiation factor 4E binding activity; and protein domain specific binding activity. Involved in nuclear-transcribed mRNA catabolic process, non-stop decay. Located in several cellular components, including cis-Golgi network; endoplasmic reticulum; and perinuclear region of cytoplasm. Is active in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19961) · Entrez [23357](https://www.ncbi.nlm.nih.gov/gene/23357) · UniProt [Q9UNK9](https://www.uniprot.org/uniprotkb/Q9UNK9) · Ensembl [ENSG00000013523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013523)

## Data

Gene col 275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 275); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 275]; `tensor/DDL_lfc|DDL_z.npy` [275]; `embed/gene_vectors.npy` [275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 275 or target_col == 275). Every well: [[ANGEL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANGEL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

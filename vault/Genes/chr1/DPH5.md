---
symbol: "DPH5"
type: "gene"
col: 3924
ensembl_id: "ENSG00000117543"
name: "diphthamide biosynthesis 5"
location: "1p21.2"
module: 1
arm: "+"
pooled_cpm: 9.44
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DPH5

*diphthamide biosynthesis 5* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.50× (z +11.0, q 3e-25, up in 15 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.84× (z +7.6, q 5e-12, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.536× (z -7.8, q 5e-12, down in 28 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.550× (z -7.4, q 3e-11, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOX2]] (+0.77, fdr 7e-06), [[PTCD2]] (+0.71, fdr 7e-06), [[PDCD2]] (+0.70, fdr 7e-06); moves opposite to [[TOR1B]] (-0.62, fdr 1e-05), [[FUCA1]] (-0.59, fdr 1e-05), [[MOSPD3]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +11.0 | 3e-25 | 15/19 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +10.6 | 1e-23 | 28/36 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +7.6 | 5e-12 | 29/45 (NCI-H1792, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.7 | 3e-09 | 26/47 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.3 | 1e-05 | 17/26 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +5.3 | 1e-05 | 20/47 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 8e-04 | 16/47 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.3 | 0.001 | 18/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.032 | 7/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.038 | 6/41 (SNU-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.043 | 9/46 (A-172, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.2 | 0.056 | 13/38 (LOX-IMVI, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +3.2 | 0.065 | 6/42 (CFPAC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.2 | 0.065 | 14/39 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.61×** | +3.1 | 0.072 | 4/39 (SK-MEL-2, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.077 | 11/46 (HCT15, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -7.8 | 5e-12 | 28/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.550×** | -7.4 | 3e-11 | 24/46 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -7.3 | 5e-11 | 30/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -5.3 | 1e-05 | 19/47 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -4.4 | 0.001 | 20/43 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -4.3 | 0.002 | 17/45 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.3 | 0.002 | 19/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.597×** | -3.4 | 0.056 | 13/41 (NCI-H1792, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.775×** | -3.2 | 0.099 | 8/48 (SW480, SW 1271, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.783× | -3.0 | 0.13 | 11/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -10.0) |
| [[BT-474 (line)]] | alt | 6.55 | 0 | 2 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0720× (z -9.2) |
| [[A-427 (line)]] | wt | 12.0 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.195× (z -8.9) |
| [[A549 (line)]] | wt | 7.75 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0778× (z -11.2) |
| [[J82 (line)]] | alt | 8.06 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0505× (z -14.0) |
| [[LoVo (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -9.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -8.8) |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 12.2 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0874× (z -8.6) |
| [[SW480 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOX2]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 | pathway: Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| [[PTCD2]] | +0.71 | +0.75 / +0.73 | both halves | 7e-06 | STRING 443 |
| [[PDCD2]] | +0.70 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TCERG1]] | +0.68 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[DIS3L]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[KICS2]] | +0.67 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[DCAF17]] | +0.66 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[COA7]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1B]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[FUCA1]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.57 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[NARF]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[APLP2]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SDF2]] | -0.57 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[C1QL1]] | -0.57 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity lowers DPH5's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.46× higher at baseline in the lines without TMEM92 | 0.010 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[TSEN2]] | C | TSEN2 activity raises DPH5's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.0, -37.7); signed map (0.1, -39.5). **Vector** length 75.5, 13.3% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | diphthamide biosynthesis 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,989,623-101,026,088 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-30 |
| Gene groups (HGNC) | Diphthamide biosynthesis genes; Tetrapyrrole methylase domain containing; Histidine methyltransferases |
| Reactome | 2 pathways, smallest: Synthesis of diphthamide-EEF2; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2P9](https://www.uniprot.org/uniprotkb/Q9H2P9) (Diphthine methyl ester synthase):

> S-adenosyl-L-methionine-dependent methyltransferase that catalyzes four methylations of the modified target histidine residue in translation elongation factor 2 (EF-2), to form an intermediate called diphthine methyl ester. The four successive methylation reactions represent the second step of diphthamide biosynthesis.

**Summary**, from NCBI Gene [51611](https://www.ncbi.nlm.nih.gov/gene/51611):

> This gene encodes a component of the diphthamide synthesis pathway. Diphthamide is a post-translationally modified histidine residue found only on translation elongation factor 2. It is conserved from archaebacteria to humans, and is targeted by diphtheria toxin and Pseudomonas exotoxin A to halt cellular protein synthesis. The yeast and Chinese hamster homologs of this protein catalyze the trimethylation of the histidine residue on elongation factor 2, resulting in a diphthine moiety that is …

**Accessions** — [HGNC:24270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24270) · Entrez [51611](https://www.ncbi.nlm.nih.gov/gene/51611) · UniProt [Q9H2P9](https://www.uniprot.org/uniprotkb/Q9H2P9) · Ensembl [ENSG00000117543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117543)

## Data

Gene col 3924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3924); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3924]; `tensor/DDL_lfc|DDL_z.npy` [3924]; `embed/gene_vectors.npy` [3924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3924 or target_col == 3924). Every well: [[DPH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

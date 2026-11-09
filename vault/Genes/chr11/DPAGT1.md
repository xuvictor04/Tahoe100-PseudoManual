---
symbol: "DPAGT1"
type: "gene"
col: 10232
ensembl_id: "ENSG00000172269"
name: "dolichyl-phosphate N-acetylglucosaminephosphotransferase 1"
location: "11q23.3"
module: 20
arm: "+"
pooled_cpm: 8.07
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DPAGT1

*dolichyl-phosphate N-acetylglucosaminephosphotransferase 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.47× (z +13.4, q 3e-38, up in 12 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.7, q 1e-24, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.556× (z -12.7, q 2e-34, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC5]] (+0.75, fdr 7e-06), [[LIG3]] (+0.72, fdr 7e-06), [[BPNT2]] (+0.70, fdr 7e-06); moves opposite to [[SUMO4]] (-0.72, fdr 1e-05), [[CROCCP2-1]] (-0.61, fdr 8e-06), [[JUND]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +13.4 | 3e-38 | 12/15 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +12.3 | 2e-32 | 26/29 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +11.2 | 1e-26 | 16/22 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.7 | 1e-24 | 28/42 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +6.5 | 1e-08 | 16/38 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.8 | 8e-07 | 14/36 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.2 | 0.002 | 10/47 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.29×** | +3.8 | 0.011 | 10/41 (SNU-423, HEC-1-A, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.28×** | +3.7 | 0.014 | 12/41 (HEC-1-A, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.030 | 3/44 (Hs 766T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lopinavir (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.046 | 5/47 (SW 900, KATO III, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.062 | 10/48 (HS-578T, H4, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.16× | +3.2 | 0.062 | 8/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.079 | 10/48 (HOP62, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.556×** | -12.7 | 2e-34 | 33/43 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -9.8 | 5e-20 | 30/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -4.9 | 2e-04 | 9/48 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.719×** | -4.9 | 2e-04 | 13/43 (hTERT-HPNE, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.740×** | -4.6 | 4e-04 | 15/41 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.745×** | -4.5 | 6e-04 | 13/46 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -4.4 | 0.001 | 17/47 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | **0.756×** | -4.3 | 0.001 | 10/44 (HCT15, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 0.836× | -3.9 | 0.006 | 5/48 (NCI-H1792, COLO 205, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.671×** | -3.2 | 0.075 | 9/42 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.075 | 9/45 (NCI-H1573, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.814×** | -3.2 | 0.075 | 11/45 (SW 900, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 6.13 | 0 | 4 (1 ⚠) | — | [[Clotrimazole (drug)]] 0.5 µM 0.0860× (z -9.2) |
| [[A-172 (line)]] | wt | 4.24 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 4.22 | 0 | 2 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.101× (z -9.8) |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 5.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -9.4) |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.3) |
| [[RKO (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 8.46 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0712× (z -9.9) |
| [[SW480 (line)]] | alt | 9.24 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[LIG3]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[RPN1]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 616 |
| [[PTPN18]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PRPS2]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[WRNIP1]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TBL3]] | +0.63 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[MDH2]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.63 | +0.59 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO4]] | -0.72 | -0.52 / -0.76 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.61 | -0.57 / -0.59 | both halves | 8e-06 |  |
| [[JUND]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[PPIG]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SLC31A2]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.59 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[FRG1]] | -0.59 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SEC62]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.58 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[PIM3]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPAGT1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.4, -25.5); signed map (-25.1, -42.0). **Vector** length 70.9, 11.2% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +11.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.2 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -4.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dolichyl-phosphate N-acetylglucosaminephosphotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,096,025-119,108,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPT, D11S366, DGPT, ALG7, CDG-Ij; previously DPAGT2, DPAGT |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3H5](https://www.uniprot.org/uniprotkb/Q9H3H5) (UDP-N-acetylglucosamine--dolichyl-phosphate N-acetylglucosaminephosphotransferase):

> UDP-N-acetylglucosamine--dolichyl-phosphate N-acetylglucosaminephosphotransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen …

**Summary**, from NCBI Gene [1798](https://www.ncbi.nlm.nih.gov/gene/1798):

> The protein encoded by this gene is an enzyme that catalyzes the first step in the dolichol-linked oligosaccharide pathway for glycoprotein biosynthesis. This enzyme belongs to the glycosyltransferase family 4. This protein is an integral membrane protein of the endoplasmic reticulum. The congenital disorder of glycosylation type Ij is caused by mutation in the gene encoding this enzyme. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2995) · Entrez [1798](https://www.ncbi.nlm.nih.gov/gene/1798) · UniProt [Q9H3H5](https://www.uniprot.org/uniprotkb/Q9H3H5) · Ensembl [ENSG00000172269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172269)

## Data

Gene col 10232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10232); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10232]; `tensor/DDL_lfc|DDL_z.npy` [10232]; `embed/gene_vectors.npy` [10232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10232 or target_col == 10232). Every well: [[DPAGT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPAGT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

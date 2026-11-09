---
symbol: "PHF1"
type: "gene"
col: 3373
ensembl_id: "ENSG00000112511"
name: "PHD finger protein 1"
location: "6p21.32"
module: 1
arm: "-"
pooled_cpm: 25.57
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PHF1

*PHD finger protein 1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.99× (z +8.2, q 2e-13, up in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.71× (z +6.4, q 3e-08, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.682× (z -6.4, q 5e-08, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ULK1]] (+0.69, fdr 7e-06), [[RASA4B]] (+0.68, fdr 1e-05), [[CBFA2T2]] (+0.68, fdr 7e-06); moves opposite to [[SF3B3]] (-0.71, fdr 7e-06), [[UTP15]] (-0.69, fdr 7e-06), [[SRFBP1]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.2 | 2e-13 | 40/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.6 | 6e-12 | 39/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +6.4 | 3e-08 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +6.1 | 1e-07 | 32/48 (PANC-1, C32, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +5.2 | 3e-05 | 31/48 (PANC-1, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.007 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.007 | 25/48 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.043 | 19/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.049 | 19/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.11 | 16/45 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.682×** | -6.4 | 5e-08 | 36/48 (hTERT-HPNE, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.585×** | -6.4 | 5e-08 | 33/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -6.1 | 2e-07 | 31/47 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.634×** | -5.4 | 9e-06 | 28/48 (H4, NCI-H661, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.661×** | -4.9 | 9e-05 | 26/47 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -4.9 | 9e-05 | 27/48 (NCI-H23, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.670×** | -4.8 | 2e-04 | 30/48 (NCI-H2347, A-427, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.695×** | -4.2 | 0.002 | 24/48 (RKO, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.738×** | -3.6 | 0.019 | 20/47 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.022 | 21/47 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.731×** | -3.5 | 0.022 | 21/47 (SW 1088, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.746×** | -3.5 | 0.023 | 18/47 (NCI-H460, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.815×** | -3.4 | 0.025 | 21/48 (NCI-H2347, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.743×** | -3.4 | 0.027 | 24/47 (HS-578T, SW 900, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.580×** | -3.4 | 0.027 | 21/47 (COLO 205, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.066 | 18/48 (RPMI-7951, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 41.6 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.288× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 15.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.40× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 40.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -10.5) |
| [[SW480 (line)]] | alt | 17.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.59× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[CFPAC-1 (line)]] | alt | 37.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -8.9) |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[NCI-H2347 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.446× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.10× (z +8.7) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -11.6) |
| [[SW 900 (line)]] | alt | 37.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.411× (z -8.7) |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[A-172 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK1]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[RASA4B]] | +0.68 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PGPEP1]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CBX7]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 | STRING 470 |
| [[TESK2]] | +0.64 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[MXD4]] | +0.64 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TULP3]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PPARA]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[WIPI1]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B3]] | -0.71 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[UTP15]] | -0.69 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[SRFBP1]] | -0.68 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[ATIC]] | -0.68 | -0.66 / -0.74 | both halves | 7e-06 |  |
| [[UMPS]] | -0.68 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[UTP20]] | -0.68 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[SCO1]] | -0.67 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.67 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.67 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[TRMT5]] | -0.67 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[NOL11]] | -0.66 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[PPIL1]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PHF1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.0, -41.8); signed map (-22.6, 11.6). **Vector** length 110, 29.2% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +7.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +6.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.4 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,410,399-33,416,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTF2L2, TDRD19C, PCL1 |
| Gene groups (HGNC) | PHD finger proteins; Tudor domain containing |
| Reactome | 2 pathways, smallest: PRC2 methylates histones and DNA; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O43189](https://www.uniprot.org/uniprotkb/O43189) (PHD finger protein 1):

> Polycomb group (PcG) that specifically binds histone H3 trimethylated at 'Lys-36' (H3K36me3) and recruits the PRC2 complex. Involved in DNA damage response and is recruited at double-strand breaks (DSBs). Acts by binding to H3K36me3, a mark for transcriptional activation, and recruiting the PRC2 complex: it is however unclear whether recruitment of the PRC2 complex to H3K36me3 leads to enhance or inhibit H3K27me3 methylation mediated by the PRC2 complex. According to some reports, PRC2 …

**Summary**, from NCBI Gene [5252](https://www.ncbi.nlm.nih.gov/gene/5252):

> This gene encodes a Polycomb group protein. The protein is a component of a histone H3 lysine-27 (H3K27)-specific methyltransferase complex, and functions in transcriptional repression of homeotic genes. The protein is also recruited to double-strand breaks, and reduced protein levels results in X-ray sensitivity and increased homologous recombination. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:8919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8919) · Entrez [5252](https://www.ncbi.nlm.nih.gov/gene/5252) · UniProt [O43189](https://www.uniprot.org/uniprotkb/O43189) · Ensembl [ENSG00000112511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112511)

## Data

Gene col 3373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3373); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3373]; `tensor/DDL_lfc|DDL_z.npy` [3373]; `embed/gene_vectors.npy` [3373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3373 or target_col == 3373). Every well: [[PHF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ZNF75A"
type: "gene"
col: 8480
ensembl_id: "ENSG00000162086"
name: "zinc finger protein 75A"
location: "16p13.3"
module: 11
arm: "+"
pooled_cpm: 20.57
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZNF75A

*zinc finger protein 75A* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +8.8, q 1e-15, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.531× (z -6.8, q 6e-09, down in 29 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.550× (z -6.7, q 6e-09, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF274]] (+0.80, fdr 7e-06), [[UTP3]] (+0.79, fdr 7e-06), [[EID2]] (+0.78, fdr 7e-06); moves opposite to [[RPA1]] (-0.67, fdr 7e-06), [[CRTAP]] (-0.66, fdr 7e-06), [[NDRG3]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF594]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +8.8 | 1e-15 | 32/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.7 | 3e-06 | 27/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.9 | 2e-04 | 26/47 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.006 | 22/46 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.030 | 19/47 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.049 | 19/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.062 | 14/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.092 | 17/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 1.32× | +3.1 | 0.14 | 7/46 (A-172, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.531×** | -6.8 | 6e-09 | 29/42 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -6.7 | 6e-09 | 34/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -4.8 | 2e-04 | 26/45 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -4.8 | 2e-04 | 25/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -4.4 | 0.002 | 21/35 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -3.8 | 0.012 | 20/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -3.6 | 0.023 | 19/28 (J82, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -3.6 | 0.023 | 19/46 (HepG2/C3A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.9 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 22.4 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -11.2) |
| [[A-427 (line)]] | wt | 39.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[H4 (line)]] | wt | 35.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.0590× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 41.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.201× (z -11.1) ⚠ toxic |
| [[C32 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 7.61 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0691× (z -8.8) |
| [[J82 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -15.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0763× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 15.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.274× (z -8.8) |
| [[A-172 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF274]] | +0.80 | +0.76 / +0.72 | both halves | 7e-06 | same gene group |
| [[UTP3]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[EID2]] | +0.78 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.77 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.75 | +0.81 / +0.74 | both halves | 7e-06 | same gene group |
| [[GPATCH8]] | +0.75 | +0.72 / +0.66 | both halves | 7e-06 | same gene group |
| [[LLPH]] | +0.74 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[RPP14]] | +0.74 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[MRM2]] | +0.73 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[SURF6]] | +0.73 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[HELQ]] | +0.73 | +0.80 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | -0.67 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[CRTAP]] | -0.66 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[NDRG3]] | -0.66 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ERMP1]] | -0.65 | -0.54 / -0.73 | both halves | 1e-05 |  |
| [[MGAT4A]] | -0.64 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[RNPEP]] | -0.63 | -0.56 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594]] | B | ZNF594 activity raises ZNF75A's level | lines that do not express ZNF594 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without ZNF594 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: ZNF594-DT, MIR3659HG, SYNGR1 |
| [[TBX3]] | B | TBX3 activity raises ZNF75A's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 1.11× lower at baseline in the lines without TBX3 | 0.075 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.0, 5.9); signed map (-0.1, -20.0). **Vector** length 101, 24.2% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +8.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | -6.0 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 75A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,305,406-3,318,852 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31529 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N20](https://www.uniprot.org/uniprotkb/Q96N20) (Zinc finger protein 75A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7627](https://www.ncbi.nlm.nih.gov/gene/7627):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13146) · Entrez [7627](https://www.ncbi.nlm.nih.gov/gene/7627) · UniProt [Q96N20](https://www.uniprot.org/uniprotkb/Q96N20) · Ensembl [ENSG00000162086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162086)

## Data

Gene col 8480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8480); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8480]; `tensor/DDL_lfc|DDL_z.npy` [8480]; `embed/gene_vectors.npy` [8480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8480 or target_col == 8480). Every well: [[ZNF75A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF75A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

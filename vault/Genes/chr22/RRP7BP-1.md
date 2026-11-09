---
symbol: "RRP7BP-1"
type: "gene"
col: 16550
ensembl_id: "ENSG00000291035"
name: ""
location: ""
module: 5
arm: "+"
pooled_cpm: 17.9
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RRP7BP-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.98× (z +15.9, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.767× (z -3.7, q 0.056, down in 19 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.785× (z -3.5, q 0.077, down in 13 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP7A]] (+0.76, fdr 7e-06, ⚠ same locus), [[METTL2B]] (+0.74, fdr 7e-06), [[RRP7BP]] (+0.71, fdr 7e-06, ⚠ same locus), [[GTPBP4]] (+0.63, fdr 7e-06), [[KCNJ14]] (+0.63, fdr 7e-06); moves opposite to [[FBXO8]] (-0.65, fdr 2e-05), [[AGA]] (-0.64, fdr 3e-05), [[ACBD5]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.98×** | +15.9 | 0e+00 | 44/47 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.20×** | +11.5 | 6e-28 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.18×** | +11.4 | 1e-27 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.89×** | +8.9 | 8e-17 | 35/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.80×** | +8.6 | 9e-16 | 38/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +7.2 | 4e-11 | 30/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +6.2 | 6e-08 | 28/47 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.44×** | +5.3 | 8e-06 | 21/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 4e-04 | 18/47 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.007 | 19/48 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.5 | 0.027 | 12/39 (HS-578T, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.029 | 8/48 (NCI-H1573, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.047 | 5/45 (HOP62, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.065 | 9/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +3.1 | 0.072 | 10/45 (C-33 A, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -3.7 | 0.056 | 19/44 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.7 | 0.056 | 17/47 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.077 | 13/48 (NCI-H2030, LoVo, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.643×** | -3.4 | 0.092 | 14/48 (AN3 CA, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.795×** | -3.3 | 0.092 | 11/47 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.804× | -3.2 | 0.13 | 14/44 (HCT15, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Roxadustat (drug)]] 5 µM |  | 0.808× | -3.0 | 0.22 | 16/47 (AsPC-1, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 9.26 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.94× (z +8.7) | [[Bosentan (hydrate) (drug)]] 5 µM 0.114× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 44.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.99× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 20.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.46× (z +13.6) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.214× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 28.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.318× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.17× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 27.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.26× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.05 µM 0.0672× (z -8.8) |
| [[BT-474 (line)]] | alt | 26.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.25× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -12.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0782× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0984× (z -10.3) |
| [[HS-578T (line)]] | alt | 17.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.60× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 10.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.28× (z +8.5) | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -11.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.630× (z -9.4) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.157× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -15.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 11.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.96× (z +10.1) | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7A]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | ⚠ same locus (35.4 kb, same strand: neighbours can correlate without regulation) |
| [[METTL2B]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[RRP7BP]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GTPBP4]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.63 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[MPP3]] | +0.63 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[ZNF787]] | +0.62 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TANGO6]] | +0.62 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[EIF3J]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CCDC138]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[C1orf159]] | +0.60 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[DAP3]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ZNF551]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[PUS1]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO8]] | -0.65 | -0.46 / -0.71 | both halves | 2e-05 |  |
| [[AGA]] | -0.64 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ACBD5]] | -0.63 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TAPT1]] | -0.62 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[PRCP]] | -0.61 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[LNX2]] | -0.61 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[SGCE]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.59 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[TXNDC16]] | -0.59 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CYLD]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[UBR5]] | -0.58 | -0.53 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RRP7BP-1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers RRP7BP-1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.2, -25.9); signed map (3.3, -46.5). **Vector** length 95.6, 20.9% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +15.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +4.5 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -3.5 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.0 |

## What is on record

> [!warning] No registry record
> RRP7BP-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16550); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16550]; `tensor/DDL_lfc|DDL_z.npy` [16550]; `embed/gene_vectors.npy` [16550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16550 or target_col == 16550). Every well: [[RRP7BP-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP7BP-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

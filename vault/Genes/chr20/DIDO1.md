---
symbol: "DIDO1"
type: "gene"
col: 2091
ensembl_id: "ENSG00000101191"
name: "death inducer-obliterator 1"
location: "20q13.33"
module: 15
arm: "+"
pooled_cpm: 170.47
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DIDO1

*death inducer-obliterator 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.15× (z +9.5, q 9e-19, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.588× (z -8.4, q 2e-14, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.617× (z -7.7, q 3e-12, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMPD4]] (+0.76, fdr 7e-06), [[LAMTOR5-AS1]] (+0.75, fdr 1e-04), [[EIF3F]] (+0.70, fdr 2e-05); moves opposite to [[TTBK2]] (-0.61, fdr 1e-05), [[SNAPIN]] (-0.59, fdr 4e-05), [[TIPRL]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.15×** | +9.5 | 9e-19 | 47/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +8.0 | 3e-13 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +7.1 | 2e-10 | 46/48 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +6.4 | 3e-08 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +6.1 | 1e-07 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +5.1 | 4e-05 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.9 | 9e-05 | 29/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.588×** | -8.4 | 2e-14 | 40/49 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -8.3 | 4e-14 | 37/44 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.617×** | -7.7 | 3e-12 | 46/48 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.643×** | -7.0 | 3e-10 | 44/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.652×** | -6.8 | 1e-09 | 46/48 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.698×** | -5.7 | 1e-06 | 41/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -5.5 | 3e-06 | 44/48 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.703×** | -5.4 | 5e-06 | 38/48 (AsPC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -5.3 | 6e-06 | 34/48 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.752×** | -4.5 | 3e-04 | 33/48 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -3.6 | 0.019 | 30/49 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 142 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 114 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 228 | 3 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.22× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 213 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 209 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 197 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 280 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0411× (z -39.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.502× (z -8.8) |
| [[A498 (line)]] | wt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 323 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -12.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 153 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 240 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.474× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.508× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 134 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.99× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -12.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 143 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.78× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 291 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -11.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 185 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.3) | — |
| [[LoVo (line)]] | wt | 113 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.88× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -12.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -15.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 173 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.144× (z -9.5) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 146 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 205 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[LAMTOR5-AS1]] | +0.75 | +0.36 / +0.72 | both halves | 1e-04 |  |
| [[EIF3F]] | +0.70 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[SENP3]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ACAD9]] | +0.65 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[GTF3C2-AS2]] | +0.65 | +0.14 / +0.62 | ⚠ one half (not replicated) | 0.002 |  |
| [[LY6G5B]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[RBBP4]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SNHG10]] | +0.62 | +0.25 / +0.57 | both halves | 4e-04 |  |
| [[PMPCA]] | +0.61 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[XNDC1N]] | +0.60 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[ZNF718]] | +0.60 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[VPS51]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTBK2]] | -0.61 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.59 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[TIPRL]] | -0.56 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 | STRING 964 |
| [[DHRS2]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ALAS1]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[COMMD3]] | -0.54 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD20A9P]] | -0.54 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[PITPNA-AS1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CEP290]] | -0.53 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[BTG1]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[METTL23]] | -0.53 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DIDO1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DIDO1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.6, 22.4); signed map (-9.1, -41.5). **Vector** length 99.5, 34.1% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.6 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.5 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +7.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | -1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -8.9 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | death inducer-obliterator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,877,738-62,937,952 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIO1, dJ885L7.8, FLJ11265, KIAA0333, DIO-1, BYE1; previously C20orf158, DATF1 |
| Gene groups (HGNC) | PHD finger proteins |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTC0](https://www.uniprot.org/uniprotkb/Q9BTC0) (Death-inducer obliterator 1):

> Putative transcription factor, weakly pro-apoptotic when overexpressed (By similarity). Tumor suppressor. Required for early embryonic stem cell development.; [Isoform 2]: Displaces isoform 4 at the onset of differentiation, required for repression of stemness genes.

**Summary**, from NCBI Gene [11083](https://www.ncbi.nlm.nih.gov/gene/11083):

> Apoptosis, a major form of cell death, is an efficient mechanism for eliminating unwanted cells and is of central importance for development and homeostasis in metazoan animals. In mice, the death inducer-obliterator-1 gene is upregulated by apoptotic signals and encodes a cytoplasmic protein that translocates to the nucleus upon apoptotic signal activation. When overexpressed, the mouse protein induced apoptosis in cell lines growing in vitro. This gene is similar to the mouse gene and …

**Accessions** — [HGNC:2680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2680) · Entrez [11083](https://www.ncbi.nlm.nih.gov/gene/11083) · UniProt [Q9BTC0](https://www.uniprot.org/uniprotkb/Q9BTC0) · Ensembl [ENSG00000101191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101191)

## Data

Gene col 2091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2091); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2091]; `tensor/DDL_lfc|DDL_z.npy` [2091]; `embed/gene_vectors.npy` [2091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2091 or target_col == 2091). Every well: [[DIDO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIDO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

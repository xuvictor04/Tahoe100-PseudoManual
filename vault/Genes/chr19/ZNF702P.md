---
symbol: "ZNF702P"
type: "gene"
col: 14328
ensembl_id: "ENSG00000242779"
name: "zinc finger protein 702, pseudogene"
location: "19q13.41"
module: 68
arm: "+"
pooled_cpm: 6.33
n_lines_expressing: 26
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# ZNF702P

*zinc finger protein 702, pseudogene* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.57× (z +27.8, q 0e+00, up in 21 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.167×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 900 0.125×; ⚠ transcription drop; cell-cycle shift, explains ~48% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFLAR-AS1]] (+0.63, fdr 7e-06), [[LINC01186]] (+0.63, fdr 2e-05), [[ANKRD20A5P]] (+0.63, fdr 1e-05); moves opposite to [[SDHAP1]] (-0.61, fdr 2e-05), [[OXNAD1]] (-0.61, fdr 1e-05), [[SHQ1]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[KDSR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.57×** | +27.8 | 0e+00 | 21/22 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +19.0 | 0e+00 | 17/22 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.80×** | +16.6 | 0e+00 | 2/9 (CFPAC-1, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.28×** | +15.3 | 0e+00 | 21/22 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +12.9 | 3e-36 | 10/12 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.79×** | +12.7 | 3e-35 | 21/23 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +11.7 | 2e-29 | 7/16 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.4 | 4e-15 | 17/23 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +8.3 | 6e-15 | 11/24 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.0 | 5e-14 | 11/20 (BT-474, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +8.0 | 8e-14 | 15/23 (RKO, BT-474, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.8 | 2e-13 | 13/23 (J82, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +6.8 | 5e-10 | 10/16 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.7 | 7e-10 | 8/22 (J82, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.9 | 1e-07 | 8/23 (RKO, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +5.4 | 2e-06 | 8/23 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 2e-06 | 7/21 (PANC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.8 | 4e-05 | 10/23 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.8 | 5e-05 | 4/23 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 6e-05 | 11/23 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14328.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.167×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 900 0.125×; ⚠ transcription drop; cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.760× | -3.6 | 0.14 | 6/24 (J82, RKO, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.827× | -3.5 | 0.14 | 1/24 (HT-29) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.763× | -3.3 | 0.21 | 0/23 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +17.0) | — |
| [[HT-29 (line)]] | alt | 13.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 53.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +16.8) | — |
| [[RKO (line)]] | wt | 23.5 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.19× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 6.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 5.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +13.8) | — |
| [[LoVo (line)]] | wt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +15.8) | — |
| [[NCI-H2347 (line)]] | alt | 6.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 8.72 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.125× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.945 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.640 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFLAR-AS1]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LINC01186]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ANKRD20A5P]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ARL14]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ANKRD18B]] | +0.63 | +0.62 / +0.40 | both halves | 4e-05 |  |
| [[ARAP2]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R1C]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZNF462]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ADAMTS3]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SOCS2]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SKIL]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.61 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[OXNAD1]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.61 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[INPP5B]] | -0.60 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[COG5]] | -0.59 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[SEC11A]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[MED23]] | -0.58 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[CBLB]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SDHAP2]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CCNY]] | -0.57 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[SNX1]] | -0.56 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[RARS2]] | -0.56 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF702P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDSR]] | B | ZNF702P activity lowers KDSR's level | lines that do not express ZNF702P (24) vs lines expressing it (26) | 1.31× higher at baseline in the lines without ZNF702P | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33 |
| [[ERCC6L2]] | B | ZNF702P activity lowers ERCC6L2's level | lines that do not express ZNF702P (24) vs lines expressing it (26) | 1.35× higher at baseline in the lines without ZNF702P | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33 |
| [[SCAI]] | B | ZNF702P activity lowers SCAI's level | lines that do not express ZNF702P (24) vs lines expressing it (26) | 1.21× higher at baseline in the lines without ZNF702P | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33 |
| [[PRKAA2]] | B | ZNF702P activity weakens PRKAA2's drug response | lines that do not express ZNF702P (17) vs lines expressing it (16) | the lines without ZNF702P respond 1.27× as strongly (z diff -1.17); strongest at Panobinostat 5 µM: 0.51x vs 0.70x (z diff -3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (16.9, 11.5); signed map (26.7, 5.7). **Vector** length 45.3, 8.53% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +27.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +8.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +5.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.3 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.2 | +3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 702, pseudogene |
| Locus type | pseudogene |
| Location | 19q13.41 — chr19:52,968,910-52,970,875 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | FLJ12985; previously ZNF702 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H963](https://www.uniprot.org/uniprotkb/Q9H963) (Putative zinc finger protein 702):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [79986](https://www.ncbi.nlm.nih.gov/gene/79986):

> Predicted to enable DNA-binding transcription factor activity. Predicted to be involved in DNA-templated transcription and regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25775) · Entrez [79986](https://www.ncbi.nlm.nih.gov/gene/79986) · UniProt [Q9H963](https://www.uniprot.org/uniprotkb/Q9H963) · Ensembl [ENSG00000242779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242779)

## Data

Gene col 14328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14328); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14328]; `tensor/DDL_lfc|DDL_z.npy` [14328]; `embed/gene_vectors.npy` [14328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14328 or target_col == 14328). Every well: [[ZNF702P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF702P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

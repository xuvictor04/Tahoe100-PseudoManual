---
symbol: "MALRD1"
type: "gene"
col: 12917
ensembl_id: "ENSG00000204740"
name: "MAM and LDL receptor class A domain containing 1"
location: "10p12.31"
module: 75
arm: "+"
pooled_cpm: 8.42
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# MALRD1

*MAM and LDL receptor class A domain containing 1* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.97× (z +23.3, q 0e+00, up in 22 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0489×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (HepG2/C3A 0.159×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.173×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.272×); [[TAK-901 (drug)]] 5 µM in 1 line (HepG2/C3A 0.101×); [[Methotrexate (drug)]] 0.05 µM in 1 line (A-172 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLEU7]] (+0.76, fdr 7e-06), [[MIR4300HG]] (+0.75, fdr 7e-06), [[EYS]] (+0.70, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLXDC2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DYNLRB2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.97×** | +23.3 | 0e+00 | 22/24 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.86×** | +16.2 | 0e+00 | 11/12 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.09×** | +16.0 | 0e+00 | 2/4 (SNU-423, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.91×** | +12.9 | 5e-36 | 2/5 (NCI-H2347, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +11.0 | 6e-26 | 16/25 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.55×** | +9.6 | 8e-20 | 19/28 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +8.0 | 1e-13 | 16/32 (SW480, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +6.7 | 2e-09 | 9/23 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.5 | 2e-06 | 5/22 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.6 | 2e-04 | 5/21 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.003 | 6/27 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.005 | 8/27 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.7 | 0.009 | 2/12 (A-172, LS 180) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.7 | 0.009 | 4/14 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.5 | 0.017 | 1/3 (SNU-423) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.020 | 2/29 (LoVo, SW480) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.041 | 0/21 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.050 | 7/27 (SW 900, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.050 | 6/24 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.050 | 1/20 (LoVo) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.081 | 2/29 (LOX-IMVI, SW480) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.088 | 3/26 (J82, SNU-423, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0489×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (HepG2/C3A 0.159×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.173×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.272×); [[TAK-901 (drug)]] 5 µM in 1 line (HepG2/C3A 0.101×); [[Methotrexate (drug)]] 0.05 µM in 1 line (A-172 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.8 | 0.089 | 6/33 (A-172, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 516 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0489× (z -23.4) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.272× (z -10.5) |
| [[A-172 (line)]] | wt | 5.74 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 62.1× (z +22.1) | [[Methotrexate (drug)]] 0.05 µM 0.100× (z -8.6) |
| [[LS 180 (line)]] | wt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +8.7) | — |
| [[A-427 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU7]] | +0.76 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.75 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[EYS]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[GRM8]] | +0.68 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DPP6]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.68 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[LINC02755]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[DPYD-AS1]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[RBMS3-AS3]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SLC9C1]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXDC2]] | B | PLXDC2 activity raises MALRD1's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without PLXDC2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[LIPC]] | B | LIPC activity raises MALRD1's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.41× lower at baseline in the lines without LIPC | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[PEG3]] | B | PEG3 activity raises MALRD1's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.79× lower at baseline in the lines without PEG3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNLRB2-AS1]] | B | MALRD1 activity raises DYNLRB2-AS1's level | lines that do not express MALRD1 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without MALRD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: NELL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.9, 27.6); signed map (34.0, 12.7). **Vector** length 40.2, 5.60% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +23.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +16.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | +0.1 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MAM and LDL receptor class A domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.31 — chr10:19,048,801-19,790,401 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA265G8.2, Diet1; previously C10orf112 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VYJ5](https://www.uniprot.org/uniprotkb/Q5VYJ5) (MAM and LDL-receptor class A domain-containing protein 1):

> Enhances production and/or transport of FGF19 and thus has a role in regulation of bile acid synthesis.

**Summary**, from NCBI Gene [340895](https://www.ncbi.nlm.nih.gov/gene/340895):

> This gene encodes a conserved protein that features multiple MAM (meprin-A5-protein tyrosine phosphatase mu) and LDLR A2 (low density lipoprotein receptor A2) domains. Expression of this gene is enriched in the small intestine and is upregulated during differentiation of a human cell line that exhibits properties of intestinal epithelial cells. The encoded protein has been shown to modulate production of FGF19 in a human intestinal cell line and may regulate bile acid metabolism in the liver. A …

**Accessions** — [HGNC:24331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24331) · Entrez [340895](https://www.ncbi.nlm.nih.gov/gene/340895) · UniProt [Q5VYJ5](https://www.uniprot.org/uniprotkb/Q5VYJ5) · Ensembl [ENSG00000204740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204740)

## Data

Gene col 12917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12917); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12917]; `tensor/DDL_lfc|DDL_z.npy` [12917]; `embed/gene_vectors.npy` [12917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12917 or target_col == 12917). Every well: [[MALRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MALRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

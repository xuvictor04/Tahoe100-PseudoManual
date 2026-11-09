---
symbol: "NKX3-1"
type: "gene"
col: 9405
ensembl_id: "ENSG00000167034"
name: "NK3 homeobox 1"
location: "8p21.2"
module: 14
arm: "+"
pooled_cpm: 8.2
n_lines_expressing: 37
n_dd_up: 38
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 15
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NKX3-1

*NK3 homeobox 1* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.85× (z +19.3, q 0e+00, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.584× (z -4.7, q 0.002, down in 14 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (LoVo 0.0698×); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Flumatinib (mesylate) (drug)]] 5 µM in 1 line (A-427 0.0602×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB7]] (+0.66, fdr 7e-06), [[STX11]] (+0.65, fdr 7e-06), [[LINC02605]] (+0.65, fdr 1e-05); moves opposite to [[PHKA2]] (-0.55, fdr 1e-05), [[ELP1]] (-0.54, fdr 5e-05), [[SEC63]] (-0.52, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[STX11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.85×** | +19.3 | 0e+00 | 25/30 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.50×** | +15.6 | 0e+00 | 27/32 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +13.7 | 2e-40 | 24/30 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.79×** | +13.6 | 1e-39 | 26/30 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.70×** | +12.9 | 7e-36 | 22/23 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.42×** | +10.6 | 2e-24 | 30/34 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +10.1 | 4e-22 | 23/27 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.89×** | +9.2 | 3e-18 | 30/33 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.04×** | +8.7 | 1e-16 | 29/35 (NCI-H460, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.72×** | +8.3 | 5e-15 | 23/29 (A-172, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.59×** | +8.2 | 1e-14 | 21/31 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +8.0 | 9e-14 | 26/35 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **5.77×** | +7.9 | 9e-14 | 25/31 (BT-474, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.35×** | +7.4 | 6e-12 | 23/35 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.15×** | +6.6 | 1e-09 | 23/35 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.09×** | +6.4 | 6e-09 | 25/33 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.08×** | +6.3 | 8e-09 | 20/33 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.62×** | +5.9 | 1e-07 | 22/34 (A549, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +5.7 | 4e-07 | 19/33 (A-172, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.66×** | +4.2 | 6e-04 | 14/32 (NCI-H1792, HS-578T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9405.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (LoVo 0.0698×); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Flumatinib (mesylate) (drug)]] 5 µM in 1 line (A-427 0.0602×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.584×** | -4.7 | 0.002 | 14/34 (HOP62, HS-578T, …) | rises with dose | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.660× | -3.5 | 0.15 | 9/33 (HepG2/C3A, A-172, …) | top dose only | plate-row cell shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.691× | -3.2 | 0.26 | 10/35 (SW 1088, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 24.8 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 9.90 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +13.4) | — |
| [[A498 (line)]] | wt | 21.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +15.1) | — |
| [[BT-474 (line)]] | alt | 25.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +15.8) | [[Selinexor (drug)]] 5 µM 0.240× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 35.3 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 15.1× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 3.70 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +17.1) | — |
| [[SW 900 (line)]] | alt | 12.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 10.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 6.79 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 8.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 4.52 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.8× (z +14.2) | — |
| [[J82 (line)]] | alt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +14.5) | — |
| [[Panc 03.27 (line)]] | alt | 9.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 4.36 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 44.8× (z +11.1) | — |
| [[A-427 (line)]] | wt | 4.71 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0602× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +13.1) | — |
| [[LoVo (line)]] | wt | 3.90 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0698× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 9.46 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 8.43× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 13.8× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB7]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[STX11]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[LINC02605]] | +0.65 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[GATM]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[ADORA2A]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[IRF2]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CXCL3]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[CCL5]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CSF2]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKA2]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ELP1]] | -0.54 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SEC63]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SEC23A]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | -0.51 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[NKTR]] | -0.51 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ANAPC10]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SLC25A42]] | -0.51 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[OXNAD1]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[USP48]] | -0.49 | -0.47 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NKX3-1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[EBI3]] | B | EBI3 activity raises NKX3-1's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 2.77× lower at baseline in the lines without EBI3 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises NKX3-1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without ZNF341-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[SLFN5]] | B | SLFN5 activity raises NKX3-1's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without SLFN5 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[SSTR2]] | B | SSTR2 activity strengthens NKX3-1's drug response | lines that do not express SSTR2 (15) vs lines expressing it (20) | the lines without SSTR2 respond 0.66× as strongly (z diff +2.09); strongest at Homoharringtonine 5 µM: 2.31x vs 7.88x (z diff +5.3) | 0.055 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; target measured in part of the lines; artifact flags |
| [[CD274]] | B | CD274 activity raises NKX3-1's level | lines that do not express CD274 (18) vs lines expressing it (32) | 1.85× lower at baseline in the lines without CD274 | 0.072 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[PPP4R4]] | B | PPP4R4 activity raises NKX3-1's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 2.61× lower at baseline in the lines without PPP4R4 | 0.072 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[GCNT4]] | B | GCNT4 activity raises NKX3-1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 2.36× lower at baseline in the lines without GCNT4 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CCL2]] | B | CCL2 activity raises NKX3-1's level | lines that do not express CCL2 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without CCL2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KIRREL3, ITGA8, VCAM1 |
| [[LINC01828]] | B | LINC01828 activity raises NKX3-1's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without LINC01828 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent |
| [[ARNT2]] | B | ARNT2 activity raises NKX3-1's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without ARNT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[STX11]] | B | STX11 activity raises NKX3-1's level | lines that do not express STX11 (8) vs lines expressing it (42) | 2.84× lower at baseline in the lines without STX11 | 0.096 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STX11]] | B | NKX3-1 activity raises STX11's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without NKX3-1 | 0.010 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[HLA-B]] | B | NKX3-1 activity raises HLA-B's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 3.29× lower at baseline in the lines without NKX3-1 | 0.016 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[TRAF1]] | B | NKX3-1 activity raises TRAF1's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without NKX3-1 | 0.020 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[DRAM1]] | B | NKX3-1 activity raises DRAM1's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without NKX3-1 | 0.020 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[HLA-E]] | B | NKX3-1 activity raises HLA-E's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without NKX3-1 | 0.032 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[IRF2]] | B | NKX3-1 activity raises IRF2's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without NKX3-1 | 0.035 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[LINC02605]] | B | NKX3-1 activity raises LINC02605's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.58× lower at baseline in the lines without NKX3-1 | 0.038 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[GCNT4]] | B | NKX3-1 activity raises GCNT4's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without NKX3-1 | 0.039 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[SPHK1]] | B | NKX3-1 activity raises SPHK1's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.56× lower at baseline in the lines without NKX3-1 | 0.063 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[ADORA2A]] | B | NKX3-1 activity raises ADORA2A's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without NKX3-1 | 0.066 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[GATM]] | B | NKX3-1 activity raises GATM's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without NKX3-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[PTX3]] | B | NKX3-1 activity raises PTX3's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without NKX3-1 | 0.075 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 3.3); signed map (41.2, 10.4). **Vector** length 91.9, 24.3% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chemokine receptors bind chemokines* (reactome, mean cos +0.51 to 8); *Interleukin-10 signaling* (reactome, mean cos +0.52 to 9); *Class A/1 (Rhodopsin-like receptors)* (reactome, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.8 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.6 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +12.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +8.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NK3 homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:23,678,697-23,682,938 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NKX3.1, BAPX2; previously NKX3A |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Hallmark sets | ANDROGEN_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99801](https://www.uniprot.org/uniprotkb/Q99801) (Homeobox protein Nkx-3.1):

> Transcription factor, which binds preferentially the consensus sequence 5'-TAAGT[AG]-3' and can behave as a transcriptional repressor. Plays an important role in normal prostate development, regulating proliferation of glandular epithelium and in the formation of ducts in prostate. Acts as a tumor suppressor controlling prostate carcinogenesis, as shown by the ability to inhibit proliferation and invasion activities of PC-3 prostate cancer cells.

**Summary**, from NCBI Gene [4824](https://www.ncbi.nlm.nih.gov/gene/4824):

> This gene encodes a homeobox-containing transcription factor. This transcription factor functions as a negative regulator of epithelial cell growth in prostate tissue. Aberrant expression of this gene is associated with prostate tumor progression. Alternate splicing results in multiple transcript variants of this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:7838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7838) · Entrez [4824](https://www.ncbi.nlm.nih.gov/gene/4824) · UniProt [Q99801](https://www.uniprot.org/uniprotkb/Q99801) · Ensembl [ENSG00000167034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167034)

## Data

Gene col 9405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9405); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9405]; `tensor/DDL_lfc|DDL_z.npy` [9405]; `embed/gene_vectors.npy` [9405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9405 or target_col == 9405). Every well: [[NKX3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKX3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

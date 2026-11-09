---
symbol: "TTN"
type: "gene"
col: 7909
ensembl_id: "ENSG00000155657"
name: "titin"
location: "2q31.2"
module: 75
arm: "+"
pooled_cpm: 12.54
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# TTN

*titin* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.27× (z +21.2, q 0e+00, up in 33 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.280×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0885×; ⚠ cell-cycle shift, explains ~92% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (SHP-77 0.0777×); [[Lopinavir (drug)]] 0.05 µM in 1 line (SNU-423 0.0590×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP5]] (+0.84, fdr 7e-06), [[LINC02755]] (+0.80, fdr 7e-06), [[USH2A]] (+0.79, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00922]] → it (grade B ⚠); 3 go from it, the strongest it → [[RIPOR3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.27×** | +21.2 | 0e+00 | 33/35 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +13.1 | 1e-36 | 22/36 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.65×** | +12.3 | 1e-32 | 31/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.8 | 3e-30 | 21/26 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.6 | 4e-29 | 5/7 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +6.9 | 5e-10 | 7/15 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.4 | 1e-08 | 13/36 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.1 | 7e-08 | 16/42 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +5.7 | 7e-07 | 13/43 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.0 | 4e-05 | 15/36 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 4e-04 | 12/41 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.001 | 12/40 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.0 | 0.003 | 7/30 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +3.7 | 0.009 | 7/43 (NCI-H23, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.010 | 9/39 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.015 | 5/40 (LoVo, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.015 | 9/35 (NCI-H2030, A549, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.023 | 2/39 (HS-578T, A-172) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.040 | 9/43 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.051 | 1/40 (HS-578T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7909.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.280×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0885×; ⚠ cell-cycle shift, explains ~92% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (SHP-77 0.0777×); [[Lopinavir (drug)]] 0.05 µM in 1 line (SNU-423 0.0590×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.6 | 0.18 | 4/44 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.766× | -3.4 | 0.19 | 5/42 (SW1417, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 6.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 4.74 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +10.7) | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0885× (z -8.9) ⚠ cell-cycle shift, explains ~92% of this change |
| [[A549 (line)]] | wt | 3.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +8.9) | — |
| [[C32 (line)]] | wt | 3.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 5.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +9.4) | — |
| [[J82 (line)]] | alt | 3.94 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0894× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 3.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +8.7) | — |
| [[RKO (line)]] | wt | 496 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.2) |
| [[SHP-77 (line)]] | alt | 4.80 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0777× (z -8.6) |
| [[SNU-423 (line)]] | alt | 4.31 | 0 | 1 | — | [[Lopinavir (drug)]] 0.05 µM 0.0590× (z -8.5) |
| [[SW 900 (line)]] | alt | 5.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0739× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 5.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +10.2) | — |
| [[A-172 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP5]] | +0.84 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC02755]] | +0.80 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[USH2A]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 | same gene group |
| [[ASB14]] | +0.79 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.78 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[TPTE2P6]] | +0.78 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.77 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.76 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[C8orf34]] | +0.76 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.76 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[DLEU7]] | +0.76 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.75 | +0.73 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00922]] | B | LINC00922 activity raises TTN's level | lines that do not express LINC00922 (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without LINC00922 | 0.062 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[LINC02932]] | B | LINC02932 activity raises TTN's level | lines that do not express LINC02932 (5) vs lines expressing it (45) | 1.40× lower at baseline in the lines without LINC02932 | 0.077 | ⚠ within organs, on part of the lines; also absent: RBFOX1, DNAH6, ESRRB; maybe low, not absent |
| [[LINC01811]] | B | LINC01811 activity raises TTN's level | lines that do not express LINC01811 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without LINC01811 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, MGC4859, XIRP2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIPOR3]] | C | TTN activity lowers RIPOR3's level | lines that do not express TTN (4) vs lines expressing it (46) | 2.65× higher at baseline in the lines without TTN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZSWIM5; maybe low, not absent; its own permutation p |
| [[NDUFV2-AS1]] | C | TTN activity lowers NDUFV2-AS1's level | lines that do not express TTN (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without TTN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZSWIM5; maybe low, not absent; its own permutation p |
| [[HSD11B1-AS1]] | C | TTN's natural level weakens HSD11B1-AS1's drug response | TTN's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.47; direction clear | 0.063 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.3, 27.3); signed map (33.3, 11.7). **Vector** length 43.3, 4.61% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +21.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.7 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | titin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:178,525,989-178,830,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CMPD4, FLJ32040, TMD, CMH9, LGMD2J, MYLK5; previously CMD1G |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Myosin light chain kinase family |
| Reactome | 6 pathways, smallest: Striated Muscle Contraction; Platelet degranulation; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ42](https://www.uniprot.org/uniprotkb/Q8WZ42) (Titin):

> Key component in the assembly and functioning of vertebrate striated muscles. By providing connections at the level of individual microfilaments, it contributes to the fine balance of forces between the two halves of the sarcomere. The size and extensibility of the cross-links are the main determinants of sarcomere extensibility properties of muscle. In non-muscle cells, seems to play a role in chromosome condensation and chromosome segregation during mitosis. Might link the lamina network to …

**Summary**, from NCBI Gene [7273](https://www.ncbi.nlm.nih.gov/gene/7273):

> This gene encodes a large abundant protein of striated muscle. The product of this gene is divided into two regions, a N-terminal I-band and a C-terminal A-band. The I-band, which is the elastic part of the molecule, contains two regions of tandem immunoglobulin domains on either side of a PEVK region that is rich in proline, glutamate, valine and lysine. The A-band, which is thought to act as a protein-ruler, contains a mixture of immunoglobulin and fibronectin repeats, and possesses kinase …

**Accessions** — [HGNC:12403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12403) · Entrez [7273](https://www.ncbi.nlm.nih.gov/gene/7273) · UniProt [Q8WZ42](https://www.uniprot.org/uniprotkb/Q8WZ42) · Ensembl [ENSG00000155657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155657)

## Data

Gene col 7909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7909); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7909]; `tensor/DDL_lfc|DDL_z.npy` [7909]; `embed/gene_vectors.npy` [7909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7909 or target_col == 7909). Every well: [[TTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

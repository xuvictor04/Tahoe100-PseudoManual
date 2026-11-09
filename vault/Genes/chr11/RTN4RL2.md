---
symbol: "RTN4RL2"
type: "gene"
col: 11868
ensembl_id: "ENSG00000186907"
name: "reticulon 4 receptor like 2"
location: "11q12.1"
module: 14
arm: "+"
pooled_cpm: 4.13
n_lines_expressing: 39
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RTN4RL2

*reticulon 4 receptor like 2* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.53× (z +11.9, q 6e-30, up in 26 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.0898×, HS-578T 0.0684×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.202×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.217×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (A549 0.217×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (HOP62 0.0845×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYRIA]] (+0.62, fdr 7e-06), [[RIPK2]] (+0.62, fdr 1e-05), [[CPAMD8]] (+0.60, fdr 1e-05); moves opposite to [[HECTD1]] (-0.50, fdr 4e-05), [[XRCC5]] (-0.49, fdr 2e-05), [[ZMYND11]] (-0.48, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MEIOB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.53×** | +11.9 | 6e-30 | 26/35 (NCI-H1792, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.58×** | +8.6 | 2e-15 | 22/34 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.64×** | +7.9 | 5e-13 | 21/31 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +7.0 | 5e-10 | 17/35 (LOX-IMVI, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +6.6 | 6e-09 | 15/34 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +5.8 | 5e-07 | 15/34 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +5.8 | 6e-07 | 7/26 (NCI-H1792, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.2 | 2e-05 | 1/7 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.8 | 1e-04 | 1/11 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 9/28 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.63×** | +4.5 | 4e-04 | 9/33 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.4 | 4e-04 | 2/15 (RKO, HS-578T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.5 | 0.017 | 0/21 | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.019 | 7/33 (HOP62, A498, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.023 | 4/33 (RKO, A498, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.046 | 2/13 (NCI-H1792, A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11868.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.0898×, HS-578T 0.0684×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.202×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.217×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (A549 0.217×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (HOP62 0.0845×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.685× | -3.4 | 0.33 | 10/34 (A549, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.718× | -3.0 | 0.40 | 8/33 (RPMI-7951, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 46.5 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.3) |
| [[HOP62 (line)]] | alt | 5.71 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0845× (z -8.6) |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0684× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0966× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.833 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYRIA]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[RIPK2]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[CPAMD8]] | +0.60 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[ADAM7-AS1]] | +0.60 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SLC30A4]] | +0.58 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[LRCH2]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NEURL3]] | +0.58 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[CRTAC1]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[C15orf48]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[LRP1]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[RAB8B]] | +0.56 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[IL1A]] | +0.56 | +0.48 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECTD1]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[XRCC5]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZMYND11]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ATR]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[NSD1]] | -0.48 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[PSME3]] | -0.47 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[PARVA]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[GNL3L]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZNF236]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[AVEN]] | -0.46 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[MCM3AP]] | -0.46 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity raises RTN4RL2's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.03× lower at baseline in the lines without G0S2 | 0.017 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[ITIH5]] | B | ITIH5 activity raises RTN4RL2's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without ITIH5 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |
| [[REEP2]] | B | REEP2 activity raises RTN4RL2's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without REEP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIOB]] | B | RTN4RL2 activity lowers MEIOB's level | lines that do not express RTN4RL2 (11) vs lines expressing it (39) | 1.53× higher at baseline in the lines without RTN4RL2 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.446). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, 0.5); signed map (43.3, 11.8). **Vector** length 59.5, 11.4% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +8.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 4 receptor like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,460,528-57,477,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NgR2, NGRH1 |
| Gene groups (HGNC) | Reticulon 4 receptor family |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UN3](https://www.uniprot.org/uniprotkb/Q86UN3) (Reticulon-4 receptor-like 2):

> Cell surface receptor that plays a functionally redundant role in the inhibition of neurite outgrowth mediated by MAG (By similarity). Plays a functionally redundant role in postnatal brain development. Contributes to normal axon migration across the brain midline and normal formation of the corpus callosum. Does not seem to play a significant role in regulating axon regeneration in the adult central nervous system. Protects motoneurons against apoptosis; protection against apoptosis is …

**Summary**, from NCBI Gene [349667](https://www.ncbi.nlm.nih.gov/gene/349667):

> Enables signaling receptor activity. Predicted to be involved in cell surface receptor signaling pathway; negative regulation of neuron projection development; and positive regulation of synapse assembly. Located in cell surface and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23053) · Entrez [349667](https://www.ncbi.nlm.nih.gov/gene/349667) · UniProt [Q86UN3](https://www.uniprot.org/uniprotkb/Q86UN3) · Ensembl [ENSG00000186907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186907)

## Data

Gene col 11868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11868); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11868]; `tensor/DDL_lfc|DDL_z.npy` [11868]; `embed/gene_vectors.npy` [11868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11868 or target_col == 11868). Every well: [[RTN4RL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN4RL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

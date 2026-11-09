---
symbol: "ERVK13-1"
type: "gene"
col: 15291
ensembl_id: "ENSG00000260565"
name: "endogenous retrovirus group K13 member 1"
location: "16p13.3"
module: 15
arm: "+"
pooled_cpm: 11.26
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ERVK13-1

*endogenous retrovirus group K13 member 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +15.5, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.639× (z -5.2, q 1e-04, down in 26 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.680× (z -4.5, q 0.002, down in 20 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Almonertinib (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.124×); [[Altretamine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0572×); [[Trimetrexate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0635×).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LENG8-AS1]] (+0.67, fdr 3e-05), [[LY6G5B]] (+0.67, fdr 3e-04), [[WDR45]] (+0.64, fdr 1e-05); moves opposite to [[HPF1]] (-0.62, fdr 0.001, ⚠ one half only (not replicated)), [[TCAF1]] (-0.62, fdr 0.001, ⚠ one half only (not replicated)), [[C15orf61]] (-0.62, fdr 3e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[PET117]] (-0.61, fdr 1e-04), [[CDC14B]] (-0.60, fdr 1e-05), [[SLC11A2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +15.5 | 0e+00 | 45/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +13.4 | 2e-38 | 44/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +10.7 | 2e-24 | 44/47 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +9.2 | 7e-18 | 43/47 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +9.1 | 9e-18 | 21/29 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +7.6 | 3e-12 | 33/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.9 | 4e-10 | 33/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +6.5 | 6e-09 | 29/45 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 2e-04 | 20/44 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.4 | 5e-04 | 19/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.4 | 5e-04 | 14/35 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +4.0 | 0.003 | 18/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.009 | 16/45 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.035 | 12/47 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.3 | 0.042 | 7/23 (RPMI-7951, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Almonertinib (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.124×); [[Altretamine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0572×); [[Trimetrexate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0635×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.639×** | -5.2 | 1e-04 | 26/46 (SNU-423, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -4.5 | 0.002 | 20/46 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.686×** | -4.2 | 0.004 | 19/46 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -3.9 | 0.013 | 18/48 (SW48, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | 0.745× | -3.3 | 0.11 | 20/40 (HOP62, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 22.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 7.80 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 8.77 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +11.5) | — |
| [[A-172 (line)]] | wt | 14.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.193× (z -8.6) |
| [[A549 (line)]] | wt | 8.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.154× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 7.18 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0635× (z -9.1) |
| [[HS-578T (line)]] | alt | 8.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 6.83 | 0 | 1 | — | [[Altretamine (drug)]] 5 µM 0.0572× (z -9.4) |
| [[KATO III (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +8.5) | — |
| [[LoVo (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 5.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 7.91 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -8.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.124× (z -11.1) |
| [[SW480 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.4) | — |
| [[A-427 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8-AS1]] | +0.67 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[LY6G5B]] | +0.67 | +0.27 / +0.68 | both halves | 3e-04 |  |
| [[WDR45]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DCTN5]] | +0.62 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[EXOC7]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[QRICH2]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RABL2A]] | +0.61 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ACAD9]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MYLK4]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 13 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | -0.62 | -0.16 / -0.70 | ⚠ one half (not replicated) | 0.001 |  |
| [[TCAF1]] | -0.62 | -0.16 / -0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[C15orf61]] ⚠ | -0.62 | -0.46 / -0.56 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PET117]] | -0.61 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[CDC14B]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | -0.60 | -0.15 / -0.57 | ⚠ one half (not replicated) | 0.001 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC11A2]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TTBK2]] | -0.59 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[LSM2]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SUMO4]] | -0.58 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[LEO1]] | -0.57 | -0.23 / -0.62 | both halves | 5e-04 |  |
| [[SLC25A4]] | -0.56 | -0.19 / -0.56 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MRPL14]] | -0.56 | -0.23 / -0.61 | both halves | 5e-04 |  |
| [[SCML2]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TPST1]] | -0.55 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[MTF2]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.54 | -0.51 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERVK13-1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SCML2]] | B | SCML2 activity lowers ERVK13-1's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without SCML2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |
| [[PITX2]] | B | PITX2 activity weakens ERVK13-1's drug response | lines that do not express PITX2 (14) vs lines expressing it (34) | the lines without PITX2 respond 1.14× as strongly (z diff -0.40); strongest at Dinaciclib 0.05 µM: 2.56x vs 1.96x (z diff -1.6) | 0.090 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |
| [[WDR17]] | B | WDR17 activity lowers ERVK13-1's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without WDR17 | 0.091 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.4, 19.9); signed map (28.6, -17.3). **Vector** length 67.1, 11.2% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +15.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.2 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.9 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | endogenous retrovirus group K13 member 1 |
| Locus type | endogenous retrovirus (other) |
| Location | 16p13.3 — chr16:2,660,348-2,682,398 (-) |
| Ensembl biotype | lncRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX77](https://www.uniprot.org/uniprotkb/Q9NX77) (Endogenous retrovirus group K member 13-1 Env polyprotein):

> Retroviral envelope proteins mediate receptor recognition and membrane fusion during early infection. Endogenous envelope proteins may have kept, lost or modified their original function during evolution (By similarity).; SU mediates receptor recognition.; TM anchors the envelope heterodimer to the viral membrane through one transmembrane domain. The other hydrophobic domain, called fusion peptide, mediates fusion of the viral membrane with the target cell membrane (By similarity).

**Summary**, from NCBI Gene [100507321](https://www.ncbi.nlm.nih.gov/gene/100507321):

> Predicted to enable structural molecule activity. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27548) · Entrez [100507321](https://www.ncbi.nlm.nih.gov/gene/100507321) · UniProt [Q9NX77](https://www.uniprot.org/uniprotkb/Q9NX77) · Ensembl [ENSG00000260565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260565)

## Data

Gene col 15291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15291); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15291]; `tensor/DDL_lfc|DDL_z.npy` [15291]; `embed/gene_vectors.npy` [15291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15291 or target_col == 15291). Every well: [[ERVK13-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERVK13-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

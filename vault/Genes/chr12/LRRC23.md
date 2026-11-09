---
symbol: "LRRC23"
type: "gene"
col: 213
ensembl_id: "ENSG00000010626"
name: "leucine rich repeat containing 23"
location: "12p13.31"
module: 38
arm: "+"
pooled_cpm: 64.96
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# LRRC23

*leucine rich repeat containing 23* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.50× (z +19.8, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.636× (z -4.1, q 0.028, down in 30 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.0937×, C-33 A 0.199×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.253×, LOX-IMVI 0.242×; ⚠ toxic); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.129×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.291×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYGM]] (+0.83, fdr 7e-06), [[TRIM72]] (+0.81, fdr 7e-06), [[LDHC]] (+0.77, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAG3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.50×** | +19.8 | 0e+00 | 48/49 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.53×** | +11.8 | 2e-29 | 46/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +10.6 | 8e-24 | 39/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.72×** | +5.1 | 6e-05 | 33/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.5 | 9e-04 | 32/47 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.013 | 31/49 (C-33 A, RPMI-7951, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.52×** | +3.7 | 0.013 | 27/50 (LoVo, LS 180, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.16×** | +3.7 | 0.013 | 31/48 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.7 | 0.016 | 28/48 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.023 | 28/49 (KATO III, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.44×** | +3.4 | 0.034 | 27/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.044 | 31/48 (A498, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.48×** | +3.3 | 0.049 | 23/48 (KATO III, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.92×** | +3.2 | 0.059 | 28/48 (NCI-H23, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.059 | 23/48 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.100 | 24/48 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 213.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.0937×, C-33 A 0.199×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.253×, LOX-IMVI 0.242×; ⚠ toxic); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.129×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.291×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -4.1 | 0.028 | 30/47 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.688× | -3.5 | 0.14 | 26/48 (J82, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.665× | -3.4 | 0.14 | 24/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.692× | -3.3 | 0.14 | 24/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.703× | -3.2 | 0.18 | 23/47 (C-33 A, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 89.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.28× (z +20.1) | — |
| [[HS-578T (line)]] | alt | 36.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +19.7) | — |
| [[SK-MEL-2 (line)]] | alt | 78.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +12.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.253× (z -9.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 45.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 39.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 96.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.78× (z +15.4) | — |
| [[LoVo (line)]] | wt | 109 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +16.8) | — |
| [[LOX-IMVI (line)]] | wt | 72.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +16.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -9.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 20.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.1 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 63.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +15.0) | — |
| [[NCI-H460 (line)]] | wt | 44.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +20.4) | — |
| [[SW 900 (line)]] | alt | 99.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +14.0) | — |
| [[SW480 (line)]] | alt | 64.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +17.6) | — |
| [[A498 (line)]] | wt | 61.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +21.4) | — |
| [[C-33 A (line)]] | alt | 82.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 55.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +12.7) | — |
| [[H4 (line)]] | wt | 97.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +13.9) | — |
| [[HCT15 (line)]] | alt | 128 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 79.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 72.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +14.5) | — |
| [[J82 (line)]] | alt | 57.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +12.2) | [[Digitoxin (drug)]] 5 µM 0.281× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 41.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +19.2) | — |
| [[NCI-H2030 (line)]] | alt | 70.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 160 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -17.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 51.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 40.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +17.0) | [[Digitoxin (drug)]] 0.5 µM 0.291× (z -9.2) |
| [[SW48 (line)]] | wt | 48.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +13.2) | — |
| [[A549 (line)]] | wt | 51.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +20.4) | — |
| [[AsPC-1 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.68× (z +21.1) | — |
| [[BT-474 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +10.3) | — |
| [[C32 (line)]] | wt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 82.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +14.1) | — |
| [[Hs 766T (line)]] | wt | 33.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +16.7) | — |
| [[NCI-H596 (line)]] | alt | 71.4 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.129× (z -11.0) |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0568× (z -8.8) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 76.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +12.6) | — |
| [[RKO (line)]] | wt | 52.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +15.0) | — |
| [[RPMI-7951 (line)]] | alt | 66.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 40.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +15.7) | — |
| [[SW 1271 (line)]] | alt | 90.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.4) | — |
| [[A-427 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGM]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[LDHC]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.76 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[SPSB2]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MIR9-1HG]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[DOK3]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ROPN1L]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ARL9]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[VWCE]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAG3]] | B | LAG3 activity raises LRRC23's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without LAG3 | 0.059 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -17.6); signed map (15.1, 12.0). **Vector** length 146, 51.7% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +11.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +5.5 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +19.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +2.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.0 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.2 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.8 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -5.1 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,873,569-6,914,241 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B7, LRPB7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53EV4](https://www.uniprot.org/uniprotkb/Q53EV4) (Leucine-rich repeat-containing protein 23):

> Essential for sperm motility and male fertility. Plays an important role in the proper assembly of the third radial spoke (RS3) head and the bridge structure between RS2 and RS3 in the sperm flagella.

**Summary**, from NCBI Gene [10233](https://www.ncbi.nlm.nih.gov/gene/10233):

> Involved in flagellated sperm motility and radial spoke assembly. Located in cytoplasm and sperm flagellum. Implicated in spermatogenic failure 92. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19138) · Entrez [10233](https://www.ncbi.nlm.nih.gov/gene/10233) · UniProt [Q53EV4](https://www.uniprot.org/uniprotkb/Q53EV4) · Ensembl [ENSG00000010626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010626)

## Data

Gene col 213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 213); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 213]; `tensor/DDL_lfc|DDL_z.npy` [213]; `embed/gene_vectors.npy` [213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 213 or target_col == 213). Every well: [[LRRC23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

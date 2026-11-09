---
symbol: "NFKBIZ"
type: "gene"
col: 6929
ensembl_id: "ENSG00000144802"
name: "NFKB inhibitor zeta"
location: "3q12.3"
module: 14
arm: "+"
pooled_cpm: 164.35
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NFKBIZ

*NFKB inhibitor zeta* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.08× (z +21.5, q 0e+00, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.483× (z -13.9, q 3e-41, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUNB]] (+0.68, fdr 7e-06), [[TRIB1]] (+0.66, fdr 7e-06), [[PTGER4]] (+0.66, fdr 7e-06); moves opposite to [[CAPN15]] (-0.55, fdr 2e-05), [[TMEM11-DT]] (-0.54, fdr 1e-05), [[DGCR2]] (-0.52, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PTGS2]] → it (grade B ⚠); 6 go from it, the strongest it → [[NFKBIA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.08×** | +21.5 | 0e+00 | 37/45 (hTERT-HPNE, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.29×** | +13.0 | 3e-36 | 45/46 (HOP62, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +12.3 | 3e-32 | 34/45 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.2 | 1e-10 | 32/45 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +6.6 | 6e-09 | 31/45 (hTERT-HPNE, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 8e-05 | 30/46 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +4.4 | 9e-04 | 23/45 (HEC-1-A, A498, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.20× | +3.4 | 0.036 | 20/46 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.036 | 23/45 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.4 | 0.036 | 21/44 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.4 | 0.040 | 20/36 (LOX-IMVI, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.483×** | -13.9 | 3e-41 | 37/46 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.513×** | -8.7 | 1e-15 | 37/45 (HT-29, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -7.5 | 1e-11 | 28/40 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -7.4 | 2e-11 | 33/47 (HT-29, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.705×** | -6.7 | 3e-09 | 33/45 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.637×** | -6.1 | 1e-07 | 28/46 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.649×** | -5.9 | 4e-07 | 33/45 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.661×** | -5.6 | 1e-06 | 34/45 (NCI-H2347, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.468×** | -5.4 | 5e-06 | 32/44 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -4.7 | 1e-04 | 27/45 (A549, C32, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -4.4 | 5e-04 | 27/45 (C32, SW 900, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.825×** | -3.7 | 0.012 | 22/45 (NCI-H23, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.769×** | -3.5 | 0.017 | 23/45 (NCI-H23, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.778×** | -3.4 | 0.027 | 21/45 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.841× | -3.3 | 0.036 | 19/45 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.842× | -3.3 | 0.037 | 20/46 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.720×** | -3.2 | 0.043 | 18/45 (HS-578T, HepG2/C3A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 236 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.50× (z +26.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 360 | 2 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 9.60× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 85.4 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.4) | — |
| [[A-172 (line)]] | wt | 173 | 4 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -10.1) |
| [[HT-29 (line)]] | alt | 370 | 3 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.54× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -17.6) |
| [[SNU-423 (line)]] | alt | 216 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 90.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +24.5) | — |
| [[HOP62 (line)]] | alt | 201 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +22.5) | [[Ixazomib citrate (drug)]] 5 µM 0.354× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -8.9) |
| [[HS-578T (line)]] | alt | 253 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.249× (z -11.7) |
| [[SW 900 (line)]] | alt | 279 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -14.5) |
| [[BT-474 (line)]] | alt | 146 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -13.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 242 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.6× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -22.7) |
| [[Hs 766T (line)]] | wt | 157 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.3) |
| [[LoVo (line)]] | wt | 148 | 4 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.79× (z +9.5) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 1.99× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -9.5) |
| [[A-427 (line)]] | wt | 83.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +20.1) | — |
| [[A498 (line)]] | wt | 195 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +21.8) | — |
| [[A549 (line)]] | wt | 172 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -10.7) |
| [[J82 (line)]] | alt | 254 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +18.0) | [[Ponatinib (drug)]] 5 µM 0.372× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 141 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 15.7× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 191 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +21.0) | — |
| [[SHP-77 (line)]] | alt | 174 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.1) |
| [[SW1417 (line)]] | alt | 119 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 95.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +25.9) | — |
| [[PANC-1 (line)]] | alt | 113 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.8) |
| [[RKO (line)]] | wt | 219 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.80× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 151 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 7.44× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.71× (z +11.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 14.1× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 336 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +24.3) | — |
| [[H4 (line)]] | wt | 136 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.1) |
| [[LS 180 (line)]] | wt | 147 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 267 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +17.4) | — |
| [[CHP-212 (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -10.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 170 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.24× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 88.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 45.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +12.5) | — |
| [[SW 1088 (line)]] | alt | 208 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +10.7) | — |
| [[SW48 (line)]] | wt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | +0.68 | +0.67 / +0.71 | both halves | 7e-06 | STRING 575 |
| [[TRIB1]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PTGER4]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[IER3]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 | STRING 531 |
| [[TNFAIP3]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 | STRING 788 |
| [[CSRNP1]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 | STRING 543 |
| [[NOCT]] | +0.61 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZC3H12A]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 | STRING 831 |
| [[SOCS3]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 | STRING 626 |
| [[HES1]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CXCL2]] | +0.60 | +0.54 / +0.69 | both halves | 1e-05 | STRING 701 |
| [[NCOA7]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN15]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TMEM11-DT]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[DGCR2]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[THAP4]] | -0.51 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[MFSD8]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[C8orf76]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[BABAM1]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[DHX35]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | -0.50 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[GLRX3]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[VKORC1L1]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[NUP133]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGS2]] | B | PTGS2 activity raises NFKBIZ's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.02× lower at baseline in the lines without PTGS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[GEM]] | B | GEM activity raises NFKBIZ's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.24× lower at baseline in the lines without GEM | 0.012 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[G0S2]] | B | G0S2 activity raises NFKBIZ's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without G0S2 | 0.015 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[TOP2A]] | B | TOP2A activity raises NFKBIZ's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ETS2]] | B | ETS2 activity raises NFKBIZ's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without ETS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[TRIB1]] | B | TRIB1 activity raises NFKBIZ's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.60× lower at baseline in the lines without TRIB1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[TLE4]] | B | TLE4 activity raises NFKBIZ's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without TLE4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFKBIA]] | C | NFKBIZ activity raises NFKBIA's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 3.45× lower at baseline in the lines without NFKBIZ | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |
| [[NFKB1]] | C | NFKBIZ activity raises NFKB1's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without NFKBIZ | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |
| [[HIVEP2]] | C | NFKBIZ activity raises HIVEP2's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without NFKBIZ | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |
| [[BIRC3]] | C | NFKBIZ activity raises BIRC3's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 3.82× lower at baseline in the lines without NFKBIZ | 0.062 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |
| [[CTNNB1]] | C | NFKBIZ activity lowers CTNNB1's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 2.34× higher at baseline in the lines without NFKBIZ | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |
| [[NOCT]] | C | NFKBIZ activity raises NOCT's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without NFKBIZ | 0.071 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, 6.4); signed map (9.8, 28.3). **Vector** length 133, 44.2% of its response variance represented; |z| ≥ 3 in 1,459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +21.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.8 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.4 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +2.2 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.3 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +0.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.8 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.7 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -4.4 |
|  | [[NG25 (drug)]] 5 µM |  | -5.1 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.8 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor zeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,827,991-101,861,022 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAIL, FLJ34463, INAP |
| Gene groups (HGNC) | Ankyrin repeat domain containing; NFKB inhibitor family |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYH8](https://www.uniprot.org/uniprotkb/Q9BYH8) (NF-kappa-B inhibitor zeta):

> Involved in regulation of NF-kappa-B transcription factor complexes. Inhibits NF-kappa-B activity without affecting its nuclear translocation upon stimulation. Inhibits DNA-binding of RELA and NFKB1/p50, and of the NF-kappa-B p65-p50 heterodimer and the NF-kappa-B p50-p50 homodimer. Also seems to activate NF-kappa-B-mediated transcription. In vitro, upon association with NFKB1/p50 has transcriptional activation activity and, together with NFKB1/p50 and RELA, is recruited to LCN2 promoters. …

**Summary**, from NCBI Gene [64332](https://www.ncbi.nlm.nih.gov/gene/64332):

> This gene is a member of the ankyrin-repeat family and is induced by lipopolysaccharide (LPS). The C-terminal portion of the encoded product which contains the ankyrin repeats, shares high sequence similarity with the I kappa B family of proteins. The latter are known to play a role in inflammatory responses to LPS by their interaction with NF-B proteins through ankyrin-repeat domains. Studies in mouse indicate that this gene product is one of the nuclear I kappa B proteins and an activator of …

**Accessions** — [HGNC:29805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29805) · Entrez [64332](https://www.ncbi.nlm.nih.gov/gene/64332) · UniProt [Q9BYH8](https://www.uniprot.org/uniprotkb/Q9BYH8) · Ensembl [ENSG00000144802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144802)

## Data

Gene col 6929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6929); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6929]; `tensor/DDL_lfc|DDL_z.npy` [6929]; `embed/gene_vectors.npy` [6929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6929 or target_col == 6929). Every well: [[NFKBIZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKBIZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

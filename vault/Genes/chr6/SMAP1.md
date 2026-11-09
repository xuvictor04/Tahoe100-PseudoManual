---
symbol: "SMAP1"
type: "gene"
col: 3353
ensembl_id: "ENSG00000112305"
name: "small ArfGAP 1"
location: "6q13"
module: 180
arm: "+"
pooled_cpm: 185.6
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# SMAP1

*small ArfGAP 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.71× (z +13.4, q 3e-38, up in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 12 lines (NCI-H23 3.07×, NCI-H2347 2.31×, SNU-1 3.43×, HCT15 3.21×, …); [[TAK-901 (drug)]] 5 µM in 2 lines (C32 3.76×, SW480 2.27×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 1.69×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.498× (z -16.7, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.606× (z -16.4, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENO2]] (+0.67, fdr 7e-06), [[FAM162A]] (+0.66, fdr 7e-06), [[SEC61G]] (+0.66, fdr 7e-06); moves opposite to [[UTP20]] (-0.56, fdr 2e-05), [[MCM7]] (-0.54, fdr 5e-05), [[PARVA]] (-0.53, fdr 4e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HK1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3353.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 12 lines (NCI-H23 3.07×, NCI-H2347 2.31×, SNU-1 3.43×, HCT15 3.21×, …); [[TAK-901 (drug)]] 5 µM in 2 lines (C32 3.76×, SW480 2.27×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 1.69×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +13.4 | 3e-38 | 46/48 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.68×** | +6.8 | 4e-09 | 40/48 (HOP62, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.19× | +4.3 | 0.003 | 20/49 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.9 | 0.014 | 14/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.029 | 15/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +3.3 | 0.092 | 3/48 (LOX-IMVI, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -16.7 | 0e+00 | 40/44 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -16.4 | 0e+00 | 42/49 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -13.2 | 2e-37 | 41/45 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.594×** | -13.0 | 3e-36 | 43/49 (NCI-H23, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.599×** | -12.8 | 3e-35 | 40/48 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.673×** | -12.7 | 4e-35 | 31/48 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.620×** | -11.9 | 9e-31 | 43/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -11.1 | 7e-27 | 43/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -10.0 | 1e-21 | 34/48 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.755×** | -9.5 | 1e-19 | 37/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.728×** | -7.9 | 1e-13 | 37/48 (HepG2/C3A, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -7.8 | 4e-13 | 29/47 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.749×** | -7.2 | 3e-11 | 36/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.770×** | -6.3 | 2e-08 | 33/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.793×** | -5.5 | 1e-06 | 29/50 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.808×** | -5.3 | 4e-06 | 25/48 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.821×** | -4.9 | 3e-05 | 24/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.840× | -4.3 | 4e-04 | 22/49 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.857× | -3.8 | 0.003 | 15/48 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.853× | -3.8 | 0.003 | 18/48 (LOX-IMVI, NCI-H2347, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.859× | -3.8 | 0.003 | 16/48 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.864× | -3.6 | 0.006 | 13/48 (H4, CFPAC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.868× | -3.5 | 0.009 | 16/48 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.871× | -3.3 | 0.019 | 12/47 (AsPC-1, SW1417, …) | top dose only | position effect removed |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.876× | -3.3 | 0.019 | 5/49 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.879× | -3.2 | 0.025 | 13/48 (HCT15, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 402 | 1 | 12 (8 ⚠) | [[Auranofin (drug)]] 5 µM 2.00× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -26.1) |
| [[J82 (line)]] | alt | 220 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -21.9) |
| [[HOP62 (line)]] | alt | 259 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -18.6) |
| [[KATO III (line)]] | alt | 253 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 229 | 1 | 7 (6 ⚠) | [[Auranofin (drug)]] 5 µM 1.95× (z +11.4) | [[Lonafarnib (drug)]] 5 µM 0.214× (z -13.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -10.2) |
| [[SW480 (line)]] | alt | 186 | 2 (1 ⚠) | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 1.61× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.483× (z -14.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 287 | 0 | 7 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.340× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.7) |
| [[HS-578T (line)]] | alt | 178 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.532× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 176 | 1 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.31× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -14.5) |
| [[A-172 (line)]] | wt | 164 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 170 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -18.3) |
| [[C32 (line)]] | wt | 200 | 1 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.76× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.250× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 222 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -22.1) |
| [[NCI-H2030 (line)]] | alt | 209 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -20.6) |
| [[RPMI-7951 (line)]] | alt | 168 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -17.2) |
| [[A549 (line)]] | wt | 181 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -16.2) |
| [[PANC-1 (line)]] | alt | 249 | 1 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.509× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 226 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -12.1) |
| [[A-427 (line)]] | wt | 129 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.75× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.503× (z -14.0) |
| [[Hs 766T (line)]] | wt | 126 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -8.6) |
| [[HT-29 (line)]] | alt | 190 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.69× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.562× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 166 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -13.1) |
| [[SNU-423 (line)]] | alt | 278 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -18.1) |
| [[AN3 CA (line)]] | alt | 353 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.372× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 164 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.38× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 208 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.43× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 152 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.25× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 269 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.07× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 293 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.9) |
| [[BT-474 (line)]] | alt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.2) |
| [[CHP-212 (line)]] | wt | 151 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.6) |
| [[HCT15 (line)]] | alt | 221 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 185 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.92× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 95.7 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0769× (z -8.8) |
| [[SW1417 (line)]] | alt | 114 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.9) |
| [[A498 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 146 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENO2]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.65 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.65 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TBC1D20]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ARFGEF3]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.62 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.62 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[RNMT]] | +0.61 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.56 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[MCM7]] | -0.54 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[PARVA]] | -0.53 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.53 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[ZNF236]] | -0.53 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MCCC2]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMAP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAPT]] | B | MAPT activity raises SMAP1's level | lines that do not express MAPT (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without MAPT | 0.026 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1 |
| [[GLRX]] | B | GLRX activity strengthens SMAP1's drug response | lines that do not express GLRX (10) vs lines expressing it (39) | the lines without GLRX respond 0.73× as strongly (z diff +1.33); strongest at Panobinostat 5 µM: 0.79x vs 0.59x (z diff +3.8) | 0.026 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PPP2R5B]] | C | PPP2R5B's natural level strengthens SMAP1's drug response | PPP2R5B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.16; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HK1]] | C | SMAP1's natural level strengthens HK1's drug response | SMAP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.32; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.6, -16.1); signed map (-36.3, 25.4). **Vector** length 126, 42.8% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.5 | +13.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.2 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | -1.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.4 | +3.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -10.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -4.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | small ArfGAP 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:70,667,776-70,862,011 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13159, SMAP-1 |
| Gene groups (HGNC) | ArfGAPs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYB5](https://www.uniprot.org/uniprotkb/Q8IYB5) (Stromal membrane-associated protein 1):

> GTPase activating protein that acts on ARF6. Plays a role in clathrin-dependent endocytosis. May play a role in erythropoiesis (By similarity).

**Summary**, from NCBI Gene [60682](https://www.ncbi.nlm.nih.gov/gene/60682):

> The protein encoded by this gene is similar to the mouse stromal membrane-associated protein-1. This similarity suggests that this human gene product is also a type II membrane glycoprotein involved in the erythropoietic stimulatory activity of stromal cells. Alternate splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19651) · Entrez [60682](https://www.ncbi.nlm.nih.gov/gene/60682) · UniProt [Q8IYB5](https://www.uniprot.org/uniprotkb/Q8IYB5) · Ensembl [ENSG00000112305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112305)

## Data

Gene col 3353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3353); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3353]; `tensor/DDL_lfc|DDL_z.npy` [3353]; `embed/gene_vectors.npy` [3353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3353 or target_col == 3353). Every well: [[SMAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

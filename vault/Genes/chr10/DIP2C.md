---
symbol: "DIP2C"
type: "gene"
col: 7499
ensembl_id: "ENSG00000151240"
name: "DIP2 acetate--CoA ligase C (putative)"
location: "10p15.3"
module: 98
arm: "+"
pooled_cpm: 162.27
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# DIP2C

*DIP2 acetate--CoA ligase C (putative)* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Budesonide (drug)]] 5 µM: 1.38× (z +5.1, q 2e-04, up in 30 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (J82 3.39×, BT-474 3.95×, HEC-1-A 3.61×, CHP-212 4.48×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Budesonide (drug)]] 5 µM in 2 lines (AsPC-1 4.22×, NCI-H1573 4.77×); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (AsPC-1 4.00×, NCI-H1573 4.56×); [[Triamcinolone (drug)]] 5 µM in 1 line (AsPC-1 2.78×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.351× (z -16.2, q 0e+00, down in 35 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -9.9, q 3e-21, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAOA]] (+0.58, fdr 1e-05), [[SNED1]] (+0.57, fdr 3e-05), [[BIN1]] (+0.56, fdr 1e-05); moves opposite to [[NCEH1]] (-0.46, fdr 3e-05), [[CD274]] (-0.44, fdr 3e-05), [[MMP13]] (-0.43, fdr 4e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7499.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (J82 3.39×, BT-474 3.95×, HEC-1-A 3.61×, CHP-212 4.48×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Budesonide (drug)]] 5 µM in 2 lines (AsPC-1 4.22×, NCI-H1573 4.77×); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (AsPC-1 4.00×, NCI-H1573 4.56×); [[Triamcinolone (drug)]] 5 µM in 1 line (AsPC-1 2.78×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | **1.38×** | +5.1 | 2e-04 | 30/44 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.15× | +3.1 | 0.30 | 5/44 (SW 900, SHP-77, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.46× | +3.1 | 0.30 | 17/44 (C32, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.30 | 20/44 (AsPC-1, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.351×** | -16.2 | 0e+00 | 35/41 (A-427, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.429×** | -13.6 | 6e-40 | 36/45 (A-172, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.467×** | -11.4 | 1e-27 | 36/42 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.485×** | -11.2 | 4e-27 | 37/43 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -9.9 | 3e-21 | 30/45 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.656×** | -6.8 | 9e-10 | 32/44 (MIA PaCa-2, C32, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -6.4 | 1e-08 | 33/44 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.670×** | -6.2 | 3e-08 | 29/46 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.698×** | -5.8 | 4e-07 | 25/44 (MIA PaCa-2, C32, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.717×** | -5.4 | 5e-06 | 34/44 (HOP62, RPMI-7951, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.726×** | -5.2 | 1e-05 | 28/44 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.1 | 1e-05 | 23/44 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.719×** | -5.1 | 1e-05 | 25/44 (NCI-H460, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.734×** | -4.8 | 6e-05 | 29/44 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.763×** | -4.4 | 5e-04 | 28/44 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.852× | -3.7 | 0.007 | 16/45 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.639×** | -3.6 | 0.008 | 25/44 (CFPAC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -3.0 | 0.070 | 16/45 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.832×** | -3.0 | 0.081 | 20/44 (RKO, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.836× | -2.9 | 0.097 | 17/45 (HOP62, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 51.7 | 25 (2 ⚠) | 0 | [[Medroxyprogesterone acetate (drug)]] 5 µM 3.04× (z +13.0) | — |
| [[A549 (line)]] | wt | 170 | 16 (1 ⚠) | 4 (4 ⚠) | [[Budesonide (drug)]] 5 µM 2.54× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 263 | 0 | 16 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 177 | 15 | 0 | [[Triamcinolone (drug)]] 5 µM 2.78× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 214 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -15.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -14.4) |
| [[HOP62 (line)]] | alt | 293 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.5) |
| [[Hs 766T (line)]] | wt | 183 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -13.7) |
| [[SHP-77 (line)]] | alt | 398 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -12.8) |
| [[SW 900 (line)]] | alt | 173 | 7 (1 ⚠) | 2 (1 ⚠) | [[Budesonide (drug)]] 5 µM 2.92× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 137 | 3 (2 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +11.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.02× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 426 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CFPAC-1 (line)]] | alt | 218 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -13.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.6) |
| [[LoVo (line)]] | wt | 122 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.238× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.472× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 172 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.285× (z -12.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 435 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.0) |
| [[A-427 (line)]] | wt | 131 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.350× (z -11.6) |
| [[A498 (line)]] | wt | 159 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 313 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.346× (z -9.1) |
| [[J82 (line)]] | alt | 117 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +19.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.291× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 148 | 1 (1 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.19× (z +10.4) ⚠ cell-cycle shift, explains ~57% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CHP-212 (line)]] | wt | 218 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.133× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 200 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -10.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.397× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 342 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 71.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.342× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -10.1) |
| [[BT-474 (line)]] | alt | 266 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 6.12× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 98.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -11.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.5) |
| [[RKO (line)]] | wt | 281 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.257× (z -14.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 350 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 201 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.523× (z -9.1) |
| [[SW480 (line)]] | alt | 66.9 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.97× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 296 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 53.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +18.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 51.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 283 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0952× (z -9.7) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAOA]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SNED1]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 | **novel candidate** |
| [[BIN1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[FLVCR2]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 | same gene group |
| [[KLF9]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TNS2]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 | same gene group |
| [[ADGRG2]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[VSTM2L]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[HIPK2]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RTN4RL1]] | +0.51 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ABCC5]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[FRMD3]] | +0.51 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCEH1]] | -0.46 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CD274]] | -0.44 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MMP13]] | -0.43 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PCED1B]] | -0.43 | -0.45 / -0.39 | both halves | 5e-05 | same gene group |
| [[CREB1]] | -0.43 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SEMA3A]] | -0.42 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[CPA4]] | -0.41 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[PKIA]] | -0.41 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[EDIL3-DT]] | -0.41 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[RASGRP3]] | -0.41 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CCNYL1]] | -0.41 | -0.38 / -0.37 | both halves | 8e-05 | same gene group |
| [[LUCAT1]] | -0.40 | -0.40 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DIP2C's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CNKSR3]] | C | CNKSR3 activity raises DIP2C's level | lines that do not express CNKSR3 (4) vs lines expressing it (46) | 3.84× lower at baseline in the lines without CNKSR3 | 0.040 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GFOD1, CMTM7, NBEAP2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | DIP2C's natural level lowers the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (makes them more sensitive) | DIP2C's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.390 over the table, 0.097 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | DIP2C's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | DIP2C's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.449 over the table, 0.068 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, 13.5); signed map (15.5, 33.0). **Vector** length 111, 35.5% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.1 | -13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.6 | -16.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.5 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.5 | +2.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.1 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.7 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.6 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.5 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | +0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | DIP2 acetate--CoA ligase C (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.3 — chr10:274,201-689,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0934 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; DIP2 family |
| Matched by | ensembl_id |

UniProt [Q9Y2E4](https://www.uniprot.org/uniprotkb/Q9Y2E4) carries no function annotation.

**Summary**, from NCBI Gene [22982](https://www.ncbi.nlm.nih.gov/gene/22982):

> This gene encodes a member of the disco-interacting protein homolog 2 family. The protein shares strong similarity with a Drosophila protein which interacts with the transcription factor disco and is expressed in the nervous system. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:29150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29150) · Entrez [22982](https://www.ncbi.nlm.nih.gov/gene/22982) · UniProt [Q9Y2E4](https://www.uniprot.org/uniprotkb/Q9Y2E4) · Ensembl [ENSG00000151240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151240)

## Data

Gene col 7499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7499); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7499]; `tensor/DDL_lfc|DDL_z.npy` [7499]; `embed/gene_vectors.npy` [7499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7499 or target_col == 7499). Every well: [[DIP2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIP2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

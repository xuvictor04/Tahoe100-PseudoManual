---
symbol: "ATP5F1B"
type: "gene"
col: 3184
ensembl_id: "ENSG00000110955"
name: "ATP synthase F1 subunit beta"
location: "12q13.3"
module: 29
arm: "+"
pooled_cpm: 166.57
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ATP5F1B

*ATP synthase F1 subunit beta* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.89× (z +18.5, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.28× (z +3.2, q 0.047, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[ULK-101 (drug)]] 0.05 µM: 0.743× (z -3.9, q 0.059, down in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.376×, C-33 A 0.480×, NCI-H23 0.526×, RKO 0.563×, …; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDH2]] (+0.77, fdr 7e-06), [[BSG]] (+0.73, fdr 7e-06), [[ATP5F1A]] (+0.72, fdr 7e-06); moves opposite to [[MAFG]] (-0.67, fdr 7e-06), [[GATAD1]] (-0.66, fdr 1e-05), [[NSRP1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LGALS3BP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.89×** | +18.5 | 0e+00 | 49/49 (A549, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.45×** | +16.2 | 0e+00 | 44/44 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.77×** | +12.3 | 2e-32 | 45/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.71×** | +7.3 | 4e-11 | 43/48 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.67×** | +6.9 | 5e-10 | 43/48 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +6.0 | 1e-07 | 40/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.55×** | +6.0 | 2e-07 | 42/48 (Panc 03.27, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.31×** | +5.1 | 2e-05 | 30/49 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.43×** | +4.8 | 1e-04 | 39/48 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.43×** | +4.7 | 2e-04 | 36/47 (LoVo, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.6 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.42×** | +4.6 | 2e-04 | 29/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.2 | 0.001 | 32/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.34×** | +3.9 | 0.003 | 28/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.71×** | +3.5 | 0.016 | 34/49 (SW480, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.047 | 30/48 (A498, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.053 | 19/48 (A-172, J82, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.054 | 35/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.066 | 23/48 (PANC-1, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[BI-78D3 (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.066 | 26/48 (HEC-1-A, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +3.0 | 0.066 | 23/48 (HT-29, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.072 | 31/47 (HCT15, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.089 | 25/47 (HCT15, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.376×, C-33 A 0.480×, NCI-H23 0.526×, RKO 0.563×, …; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[ULK-101 (drug)]] 0.05 µM |  | **0.743×** | -3.9 | 0.059 | 36/49 (H4, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.4 | 0.13 | 23/48 (A-427, C-33 A, …) | top dose only | composition shift; position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.13 | 21/48 (SNU-1, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.791× | -3.2 | 0.17 | 31/48 (HCT15, KATO III, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.625× | -3.1 | 0.21 | 24/49 (SW480, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 94.9 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 86.9 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 121 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 124 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 152 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 209 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.09× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 412 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 175 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 136 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.51× (z +17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 170 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.07× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 136 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 86.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 157 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 127 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 141 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 263 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 164 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 221 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 66.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.99× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 182 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 202 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 191 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 199 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 147 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 213 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AsPC-1 (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 242 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 231 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 191 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW48 (line)]] | wt | 262 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 194 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[BT-474 (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[COLO 205 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-1 (line)]] | wt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CHP-212 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 491 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH2]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 921 |
| [[BSG]] | +0.73 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ATP5F1A]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[PRPF8]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PRDX3]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 673 |
| [[BPNT2]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[EMC1]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 | pathway: Protein localization |
| [[SLC25A39]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[PPT1]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SNRNP200]] | +0.65 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[ERMP1]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFG]] | -0.67 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[GATAD1]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.66 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.66 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.65 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.65 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ITSN2]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[MSX1]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.63 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[AK6]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.61 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ATF4]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3BP]] | B | LGALS3BP activity lowers ATP5F1B's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.70× higher at baseline in the lines without LGALS3BP | 0.014 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[TM4SF19-DYNLT2B]] | B | TM4SF19-DYNLT2B activity lowers ATP5F1B's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 1.38× higher at baseline in the lines without TM4SF19-DYNLT2B | 0.018 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.4, -22.9); signed map (-25.9, -39.6). **Vector** length 81.8, 27.1% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +4.0 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.4 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.3 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.3 | +7.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +1.8 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -0.1 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase F1 subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,638,175-56,645,984 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATPSB, ATP5B |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits; Small nucleolar RNA protein coding host genes; ATPase F1/V1 alpha/A and beta/B subunit family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P06576](https://www.uniprot.org/uniprotkb/P06576) (ATP synthase F(1) complex subunit beta, mitochondrial):

> Catalytic subunit beta, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain (Probable). ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) …

**Summary**, from NCBI Gene [506](https://www.ncbi.nlm.nih.gov/gene/506):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:830) · Entrez [506](https://www.ncbi.nlm.nih.gov/gene/506) · UniProt [P06576](https://www.uniprot.org/uniprotkb/P06576) · Ensembl [ENSG00000110955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110955)

## Data

Gene col 3184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3184); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3184]; `tensor/DDL_lfc|DDL_z.npy` [3184]; `embed/gene_vectors.npy` [3184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3184 or target_col == 3184). Every well: [[ATP5F1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5F1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

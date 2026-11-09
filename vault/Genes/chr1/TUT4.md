---
symbol: "TUT4"
type: "gene"
col: 5595
ensembl_id: "ENSG00000134744"
name: "terminal uridylyl transferase 4"
location: "1p32.3"
module: 54
arm: "+"
pooled_cpm: 206.99
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TUT4

*terminal uridylyl transferase 4* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.15× (z +4.7, q 0.002, up in 19 of 47 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.26× (z +3.7, q 0.025, up in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 1.58×, PANC-1 1.36×, A498 1.44×; ⚠ cell-cycle shift, explains ~82% of this change); [[Triamcinolone (drug)]] 5 µM in 1 line (H4 1.66×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 1.85×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 1.83×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.509× (z -31.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHPRH]] (+0.63, fdr 8e-06), [[ATP5MC2]] (+0.63, fdr 1e-05), [[SRSF11]] (+0.63, fdr 2e-05, ⚠ SRSF11 in the vector space only through flagged drug-doses), [[HDAC8]] (+0.61, fdr 1e-05); moves opposite to [[HAPSTR1]] (-0.54, fdr 3e-05), [[ACLY]] (-0.54, fdr 3e-05), [[CDC42EP2]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5595.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 1.58×, PANC-1 1.36×, A498 1.44×; ⚠ cell-cycle shift, explains ~82% of this change); [[Triamcinolone (drug)]] 5 µM in 1 line (H4 1.66×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 1.85×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 1.83×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.7 | 0.002 | 19/47 (C-33 A, SW1417, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.14× | +4.3 | 0.005 | 13/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.9 | 0.020 | 17/47 (C-33 A, SW1417, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.025 | 22/46 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.10× | +3.1 | 0.24 | 9/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -31.3 | 0e+00 | 47/48 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.562×** | -18.9 | 0e+00 | 43/48 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -16.5 | 0e+00 | 42/47 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -16.0 | 0e+00 | 44/49 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.637×** | -13.7 | 2e-40 | 35/44 (C-33 A, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.651×** | -13.5 | 2e-39 | 35/43 (SNU-1, C-33 A, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.706×** | -11.4 | 3e-28 | 34/47 (SW480, A549, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -10.8 | 2e-25 | 41/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -9.6 | 4e-20 | 26/47 (A-172, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.756×** | -8.8 | 7e-17 | 33/46 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -8.6 | 6e-16 | 32/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **0.780×** | -8.1 | 3e-14 | 34/47 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.810×** | -6.9 | 3e-10 | 25/47 (SW480, A549, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.832×** | -6.0 | 8e-08 | 26/47 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.723×** | -5.2 | 7e-06 | 31/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.740×** | -4.8 | 5e-05 | 28/47 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.751×** | -4.6 | 1e-04 | 26/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.829×** | -4.4 | 4e-04 | 22/47 (PANC-1, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.002 | 26/46 (SW48, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.789×** | -3.8 | 0.004 | 23/48 (C32, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.886× | -3.6 | 0.007 | 13/46 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.892× | -3.5 | 0.010 | 6/47 (HCT15, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.896× | -3.4 | 0.014 | 10/47 (NCI-H1573, C32, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.902× | -3.3 | 0.018 | 5/47 (COLO 205, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 178 | 7 | 5 | [[Clobetasol propionate (drug)]] 0.05 µM 1.85× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 269 | 0 | 11 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.301× (z -19.8) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -16.6) |
| [[SW480 (line)]] | alt | 270 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -21.8) |
| [[HEC-1-A (line)]] | alt | 261 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -19.2) |
| [[HOP62 (line)]] | alt | 221 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -15.9) |
| [[NCI-H1573 (line)]] | alt | 231 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -28.0) |
| [[NCI-H23 (line)]] | alt | 270 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -19.6) |
| [[SNU-423 (line)]] | alt | 200 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -18.5) |
| [[A-172 (line)]] | wt | 206 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -17.5) |
| [[AN3 CA (line)]] | alt | 370 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 245 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -20.0) |
| [[Panc 03.27 (line)]] | alt | 210 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -21.0) |
| [[SK-MEL-2 (line)]] | alt | 205 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -13.4) |
| [[SW 900 (line)]] | alt | 199 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -18.3) |
| [[HS-578T (line)]] | alt | 214 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -25.8) |
| [[NCI-H1792 (line)]] | alt | 195 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 184 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -22.9) |
| [[PANC-1 (line)]] | alt | 292 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -22.3) |
| [[RKO (line)]] | wt | 291 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -16.4) |
| [[SW48 (line)]] | wt | 258 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -13.7) |
| [[A-427 (line)]] | wt | 270 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.7) |
| [[A549 (line)]] | wt | 191 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -19.8) |
| [[C-33 A (line)]] | alt | 367 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -11.2) |
| [[C32 (line)]] | wt | 188 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -11.4) |
| [[H4 (line)]] | wt | 304 | 1 | 3 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.66× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 265 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.6) |
| [[A498 (line)]] | wt | 147 | 2 | 1 | [[Clobetasol propionate (drug)]] 0.5 µM 1.64× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -18.7) |
| [[HCT15 (line)]] | alt | 321 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -16.6) |
| [[J82 (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -15.8) |
| [[LoVo (line)]] | wt | 185 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.536× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 230 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +12.4) ⚠ cell-cycle shift, explains ~82% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -20.8) |
| [[NCI-H2347 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -21.5) |
| [[SNU-1 (line)]] | wt | 275 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -9.8) |
| [[SW1417 (line)]] | alt | 137 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -12.9) |
| [[LS 180 (line)]] | wt | 180 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.530× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.510× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.9) |
| [[BT-474 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -22.2) |
| [[CHP-212 (line)]] | wt | 153 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.153× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.5) |
| [[SHP-77 (line)]] | alt | 251 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 9 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHPRH]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[ATP5MC2]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SRSF11]] ⚠ | +0.63 | +0.47 / +0.66 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C15orf61]] ⚠ | +0.61 | +0.51 / +0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HDAC8]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CAPN7]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MAP2K7]] | +0.58 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PHIP]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZNF235]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[LSM14A]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 | STRING 492 |
| [[ZCRB1]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 | same gene group |
| [[BRWD1]] | +0.56 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[SEC62]] | +0.55 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[GKAP1]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAPSTR1]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ACLY]] | -0.54 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[CDC42EP2]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[DDX5]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[FLNA]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PNP]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ADAT1]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CAPN2]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[CFL1]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[DBNL]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ERVK13-1]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SLC35C1]] | -0.50 | -0.39 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TUT4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.5, -11.8); signed map (-11.4, -5.3). **Vector** length 117, 35.7% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.3 | +4.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.6 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.2 | +1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.1 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -31.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.4 | -9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -16.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -8.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | terminal uridylyl transferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,408,282-52,553,487 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0191, PAPD3, TENT3A; previously ZCCHC11 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Non-canonical poly(A) polymerases; Terminal nucleotidyltransferases |
| Reactome | 6 pathways, smallest: Zygotic genome activation (ZGA); Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Deadenylation of mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TAX3](https://www.uniprot.org/uniprotkb/Q5TAX3) (Terminal uridylyltransferase 4):

> Uridylyltransferase that mediates the terminal uridylation of mRNAs with short (less than 25 nucleotides) poly(A) tails, hence facilitating global mRNA decay. Essential for both oocyte maturation and fertility. Through 3' terminal uridylation of mRNA, sculpts, with TUT7, the maternal transcriptome by eliminating transcripts during oocyte growth (By similarity). Involved in microRNA (miRNA)-induced gene silencing through uridylation of deadenylated miRNA targets. Also functions as an integral …

**Summary**, from NCBI Gene [23318](https://www.ncbi.nlm.nih.gov/gene/23318):

> Enables RNA uridylyltransferase activity. Involved in RNA metabolic process; stem cell population maintenance; and transposable element silencing by mRNA destabilization. Located in cytoplasmic ribonucleoprotein granule and cytosol. Implicated in liver benign neoplasm. Biomarker of breast cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28981) · Entrez [23318](https://www.ncbi.nlm.nih.gov/gene/23318) · UniProt [Q5TAX3](https://www.uniprot.org/uniprotkb/Q5TAX3) · Ensembl [ENSG00000134744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134744)

## Data

Gene col 5595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5595); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5595]; `tensor/DDL_lfc|DDL_z.npy` [5595]; `embed/gene_vectors.npy` [5595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5595 or target_col == 5595). Every well: [[TUT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

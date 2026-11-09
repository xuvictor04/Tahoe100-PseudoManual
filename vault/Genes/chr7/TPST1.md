---
symbol: "TPST1"
type: "gene"
col: 9869
ensembl_id: "ENSG00000169902"
name: "tyrosylprotein sulfotransferase 1"
location: "7q11.21"
module: 83
arm: "-"
pooled_cpm: 139.96
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 11
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# TPST1

*tyrosylprotein sulfotransferase 1* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +20.1, q 0e+00, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.352× (z -23.3, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.512× (z -21.1, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC14B]] (+0.60, fdr 4e-05), [[ZNF10]] (+0.58, fdr 2e-05), [[DOCK6]] (+0.58, fdr 5e-05); moves opposite to [[PSKH1]] (-0.56, fdr 3e-05), [[LINC01376]] (-0.56, fdr 3e-05), [[ERVK13-1]] (-0.55, fdr 8e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[HIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +20.1 | 0e+00 | 37/43 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +14.6 | 0e+00 | 37/43 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +13.3 | 3e-38 | 40/43 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +11.2 | 5e-27 | 35/43 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +10.2 | 2e-22 | 32/43 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +9.8 | 1e-20 | 38/43 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +9.6 | 6e-20 | 28/43 (SW480, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +8.3 | 1e-14 | 32/43 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +7.5 | 4e-12 | 34/43 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +7.3 | 1e-11 | 26/43 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +6.9 | 2e-10 | 31/43 (SNU-423, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +6.8 | 5e-10 | 30/44 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +6.0 | 9e-08 | 27/44 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.9 | 1e-07 | 26/43 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +5.2 | 6e-06 | 30/44 (NCI-H2030, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 8e-04 | 21/43 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.352×** | -23.3 | 0e+00 | 38/44 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -21.1 | 0e+00 | 38/44 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -19.8 | 0e+00 | 34/40 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.429×** | -17.5 | 0e+00 | 38/41 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -10.6 | 4e-24 | 31/45 (HS-578T, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -9.6 | 5e-20 | 33/43 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.720×** | -7.3 | 2e-11 | 30/43 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -6.5 | 6e-09 | 28/43 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.577×** | -6.4 | 9e-09 | 28/36 (BT-474, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -6.0 | 1e-07 | 24/42 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.767×** | -5.5 | 2e-06 | 26/42 (HS-578T, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.647×** | -5.1 | 2e-05 | 26/42 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -5.0 | 3e-05 | 25/43 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.709×** | -4.0 | 0.002 | 16/44 (A498, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.9 | 0.003 | 21/43 (NCI-H1792, CHP-212, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.836× | -3.8 | 0.004 | 18/44 (HS-578T, HepG2/C3A, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.734×** | -3.6 | 0.010 | 18/43 (H4, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -3.6 | 0.012 | 19/43 (PANC-1, A498, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.014 | 17/42 (CFPAC-1, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[DTP3 (drug)]] 5 µM |  | **0.759×** | -3.2 | 0.034 | 12/43 (RPMI-7951, J82, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.059 | 9/43 (A498, LoVo, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.877× | -2.9 | 0.082 | 12/43 (SHP-77, NCI-H1792, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.878× | -2.9 | 0.085 | 7/44 (C32, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 119 | 12 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +27.8) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -15.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 229 | 2 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -22.6) |
| [[PANC-1 (line)]] | alt | 140 | 5 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -21.0) |
| [[SNU-423 (line)]] | alt | 154 | 7 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +19.4) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -13.6) |
| [[SW1417 (line)]] | alt | 63.7 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +27.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 5 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 44.9 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +19.1) | — |
| [[SK-MEL-2 (line)]] | alt | 201 | 5 | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.94× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.0) |
| [[HOP62 (line)]] | alt | 175 | 2 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -16.5) |
| [[J82 (line)]] | alt | 139 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +19.3) | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.2) |
| [[A-172 (line)]] | wt | 204 | 3 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 223 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -16.4) |
| [[SNU-1 (line)]] | wt | 161 | 4 (1 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.70× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 463 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -31.7) |
| [[NCI-H2347 (line)]] | alt | 113 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +20.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -21.6) |
| [[A498 (line)]] | wt | 450 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 57.5 | 5 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.62× (z +13.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.88× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 189 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -17.5) |
| [[SW 900 (line)]] | alt | 182 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -20.1) |
| [[A-427 (line)]] | wt | 120 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0808× (z -30.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.7) |
| [[CHP-212 (line)]] | wt | 648 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0613× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 190 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.5) |
| [[SHP-77 (line)]] | alt | 195 | 3 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -25.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 79.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 222 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -14.2) |
| [[Hs 766T (line)]] | wt | 43.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 81.6 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 73.2 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.51× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -23.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 115 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +27.1) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.7) |
| [[AN3 CA (line)]] | alt | 300 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -8.8) |
| [[BT-474 (line)]] | alt | 71.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +16.2) | [[Lonafarnib (drug)]] 5 µM 0.169× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 207 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 43.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +13.4) | — |
| [[RKO (line)]] | wt | 91.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -19.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 348 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Menadione (drug)]] 0.05 µM 0.167× (z -9.4) |
| [[A549 (line)]] | wt | 84.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 144 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -18.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 154 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 81.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +19.3) | — |
| [[H4 (line)]] | wt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -12.1) |
| [[SW 1271 (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0610× (z -16.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC14B]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ZNF10]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[DOCK6]] | +0.58 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SYP]] | +0.58 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[ABAT]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TTBK2]] | +0.55 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[POLR2I]] | +0.55 | +0.20 / +0.42 | both halves | 7e-04 |  |
| [[DDX19B]] | +0.53 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[KRT10]] ⚠ | +0.53 | +0.40 / +0.45 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TUBB2B]] | +0.53 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[SLC17A5]] | +0.52 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[ARL4D]] | +0.51 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[IFI27L2]] | +0.51 | +0.44 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSKH1]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[LINC01376]] | -0.56 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ERVK13-1]] | -0.55 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[MSL3]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[MSANTD2]] | -0.53 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CRPPA]] | -0.52 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[SECISBP2]] | -0.52 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[PHC2-AS1]] | -0.52 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[CYP4V2]] | -0.52 | -0.45 / -0.37 | both halves | 9e-05 | pathway: Biological oxidations |
| [[RNF170]] | -0.51 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[RABL2A]] | -0.51 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.51 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TPST1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ASAP3]] | C | ASAP3 activity raises TPST1's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 5.60× lower at baseline in the lines without ASAP3 | 0.043 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIP1]] | B | TPST1 activity raises HIP1's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 3.89× lower at baseline in the lines without TPST1 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[MOGAT3]] | B | TPST1 activity lowers MOGAT3's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 6.13× higher at baseline in the lines without TPST1 | 0.027 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[UBE2B]] | B | TPST1 activity lowers UBE2B's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.39× higher at baseline in the lines without TPST1 | 0.045 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[PACRGL]] | B | TPST1 activity raises PACRGL's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without TPST1 | 0.051 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[TTBK2]] | B | TPST1 activity raises TTBK2's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without TPST1 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[KLHL11]] | B | TPST1 activity raises KLHL11's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without TPST1 | 0.063 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[ZNF514]] | B | TPST1 activity raises ZNF514's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without TPST1 | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[UBTF]] | B | TPST1 activity raises UBTF's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without TPST1 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[ABCF2]] | B | TPST1 activity raises ABCF2's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without TPST1 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[TSPAN33]] | B | TPST1 activity raises TSPAN33's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.96× lower at baseline in the lines without TPST1 | 0.083 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[DUS2]] | B | TPST1 activity raises DUS2's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without TPST1 | 0.087 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-6.8, 19.7); signed map (-22.9, 22.7). **Vector** length 119, 37.9% of its response variance represented; |z| ≥ 3 in 1,445 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.5 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +14.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +7.4 | +9.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.5 | +8.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -21.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -10.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | tyrosylprotein sulfotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,205,317-66,420,543 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TANGO13A |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | XENOBIOTIC_METABOLISM, GLYCOLYSIS |
| Reactome | 8 pathways, smallest: Defective F8 sulfation at Y1699; Defective factor VIII causes hemophilia A; Cytosolic sulfonation of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O60507](https://www.uniprot.org/uniprotkb/O60507) (Protein-tyrosine sulfotransferase 1):

> Catalyzes the O-sulfation of tyrosine residues within acidic motifs of polypeptides, using 3'-phosphoadenylyl sulfate (PAPS) as cosubstrate.

**Summary**, from NCBI Gene [8460](https://www.ncbi.nlm.nih.gov/gene/8460):

> Enables protein homodimerization activity and protein-tyrosine sulfotransferase activity. Involved in post-translational protein modification. Located in Golgi membrane. Implicated in colorectal adenocarcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12020) · Entrez [8460](https://www.ncbi.nlm.nih.gov/gene/8460) · UniProt [O60507](https://www.uniprot.org/uniprotkb/O60507) · Ensembl [ENSG00000169902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169902)

## Data

Gene col 9869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9869); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9869]; `tensor/DDL_lfc|DDL_z.npy` [9869]; `embed/gene_vectors.npy` [9869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9869 or target_col == 9869). Every well: [[TPST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

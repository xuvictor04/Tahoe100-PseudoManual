---
symbol: "TRIM25"
type: "gene"
col: 4249
ensembl_id: "ENSG00000121060"
name: "tripartite motif containing 25"
location: "17q22"
module: 32
arm: "+"
pooled_cpm: 117.85
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 55
direction_downstream: 24
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM25

*tripartite motif containing 25* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.37× (z +6.0, q 1e-06, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.616× (z -13.2, q 4e-37, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MX1]] (+0.73, fdr 7e-06), [[OAS3]] (+0.73, fdr 7e-06), [[PLSCR1]] (+0.72, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); 24 go from it, the strongest it → [[PML]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +6.0 | 1e-06 | 34/48 (SW480, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.6 | 7e-06 | 26/48 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.8 | 4e-04 | 25/48 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.18× | +4.5 | 0.001 | 21/48 (SW48, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.4 | 0.001 | 25/47 (J82, NCI-H23, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.003 | 25/47 (KATO III, SNU-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.006 | 19/49 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.007 | 20/49 (RPMI-7951, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +3.6 | 0.017 | 20/48 (SW48, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.14× | +3.6 | 0.017 | 11/48 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.20×** | +3.5 | 0.017 | 21/48 (C32, SW480, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.017 | 20/49 (SW1417, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.18× | +3.5 | 0.017 | 20/50 (SNU-423, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.017 | 20/49 (CFPAC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.040 | 11/49 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.2 | 0.046 | 16/48 (C32, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.046 | 18/47 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.049 | 23/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.0 | 0.083 | 8/48 (LS 180, A-172, …) | top dose only |  |
| [[Fusidic acid (drug)]] 5 µM |  | 1.11× | +2.9 | 0.091 | 2/48 (NCI-H23, SHP-77) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +2.9 | 0.091 | 20/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.616×** | -13.2 | 4e-37 | 32/49 (NCI-H23, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.710×** | -9.4 | 2e-18 | 32/49 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.634×** | -8.8 | 3e-16 | 33/48 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.642×** | -8.6 | 2e-15 | 32/49 (BT-474, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.684×** | -7.3 | 2e-11 | 29/49 (NCI-H23, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib (drug)]] 5 µM |  | **0.489×** | -7.2 | 6e-11 | 33/48 (NCI-H23, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.695×** | -7.0 | 2e-10 | 32/49 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.785×** | -6.6 | 3e-09 | 27/48 (A549, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.747×** | -5.4 | 4e-06 | 26/44 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -5.0 | 3e-05 | 25/47 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.782×** | -4.8 | 1e-04 | 28/48 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.806×** | -4.2 | 0.001 | 21/48 (RPMI-7951, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.807×** | -4.2 | 0.001 | 25/48 (NCI-H1573, NCI-H1792, …) | two highest doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.816×** | -3.8 | 0.006 | 24/49 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.816×** | -3.7 | 0.007 | 21/48 (RPMI-7951, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 0.5 µM |  | **0.826×** | -3.7 | 0.008 | 20/48 (BT-474, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.837× | -3.4 | 0.019 | 16/48 (A549, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 136 | 0 | 10 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.326× (z -13.4) |
| [[A549 (line)]] | wt | 239 | 0 | 8 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.370× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 148 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.35× (z +11.9) | [[Tofacitinib (drug)]] 5 µM 0.444× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 136 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +11.8) | [[Tofacitinib (drug)]] 5 µM 0.403× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.422× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.344× (z -15.4) |
| [[C-33 A (line)]] | alt | 135 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.323× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.566× (z -8.9) |
| [[HS-578T (line)]] | alt | 113 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.15× (z +18.3) | — |
| [[LoVo (line)]] | wt | 206 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.475× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.498× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 112 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +10.8) | [[Tofacitinib (drug)]] 5 µM 0.502× (z -10.9) |
| [[RKO (line)]] | wt | 151 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.439× (z -10.6) |
| [[SW480 (line)]] | alt | 55.9 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +15.3) | — |
| [[A-172 (line)]] | wt | 144 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.510× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 122 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 89.5 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Tofacitinib (drug)]] 5 µM 0.431× (z -10.5) |
| [[A498 (line)]] | wt | 195 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.534× (z -10.6) |
| [[C32 (line)]] | wt | 48.7 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.13× (z +9.0) | — |
| [[H4 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 57.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +8.8) | — |
| [[KATO III (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 196 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.291× (z -11.9) |
| [[COLO 205 (line)]] | alt | 237 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.422× (z -10.1) |
| [[HOP62 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[J82 (line)]] | alt | 88.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 35.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 64.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 64.7 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.376× (z -11.8) |
| [[SW 1271 (line)]] | alt | 78.1 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.100× (z -9.8) |
| [[SW48 (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.37× (z +9.0) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[A-427 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 141 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 90.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MX1]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 811 |
| [[OAS3]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 501 |
| [[PLSCR1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[DDX60L]] | +0.72 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[IFI35]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[LAMP3]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[BATF2]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PARP9]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 401 |
| [[CMPK2]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 451 |
| [[OAS1]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 534 |
| [[PARP12]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 408 |
| [[NLRC5]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 780 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 34, C 21. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises TRIM25's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without SRMS | 6e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OAS2]] | B | OAS2 activity raises TRIM25's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without OAS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PARP9]] | B | PARP9 activity raises TRIM25's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without PARP9 | 0.002 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises TRIM25's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without PLSCR1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises TRIM25's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.77× lower at baseline in the lines without CMPK2 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI6]] | B | IFI6 activity strengthens TRIM25's drug response | lines that do not express IFI6 (13) vs lines expressing it (36) | the lines without IFI6 respond 0.19× as strongly (z diff +2.53); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.92x vs 0.57x (z diff +4.2) | 0.006 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GBP4]] | B | GBP4 activity raises TRIM25's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.50× lower at baseline in the lines without GBP4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[MX1]] | B | MX1 activity raises TRIM25's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without MX1 | 0.009 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[TRIM22]] | B | TRIM22 activity raises TRIM25's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without TRIM22 | 0.012 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[OAS3]] | B | OAS3 activity raises TRIM25's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without OAS3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[ETV7]] | B | ETV7 activity raises TRIM25's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without ETV7 | 0.012 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[SRMS]] | B | SRMS activity strengthens TRIM25's drug response | lines that do not express SRMS (14) vs lines expressing it (35) | the lines without SRMS respond 0.40× as strongly (z diff +1.74); strongest at Dinaciclib 0.5 µM: 1.14x vs 0.65x (z diff +5.0) | 0.013 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PML]] | C | TRIM25's natural level strengthens PML's drug response | TRIM25's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.62; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | TRIM25's natural level strengthens PARP12's drug response | TRIM25's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.70; direction not clear | 9e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | TRIM25's natural level strengthens TDRD7's drug response | TRIM25's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.58; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFI35]] | C | TRIM25's natural level strengthens IFI35's drug response | TRIM25's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.62; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | TRIM25's natural level strengthens HELZ2's drug response | TRIM25's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.76; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | TRIM25's natural level strengthens ADAR's drug response | TRIM25's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.76; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NMI]] | C | TRIM25's natural level strengthens NMI's drug response | TRIM25's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.49; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM14]] | C | TRIM25's natural level strengthens TRIM14's drug response | TRIM25's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.81; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | TRIM25's natural level strengthens IRF9's drug response | TRIM25's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.74; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | TRIM25's natural level strengthens TRANK1's drug response | TRIM25's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.39; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[UBE2L6]] | C | TRIM25's natural level strengthens UBE2L6's drug response | TRIM25's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.44; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM21]] | C | TRIM25's natural level strengthens TRIM21's drug response | TRIM25's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.52; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.3, 55.5); signed map (64.8, 33.8). **Vector** length 143, 46.3% of its response variance represented; |z| ≥ 3 in 1,452 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.67 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.64 to 27); *IFIT antiviral response* (reactome, mean cos +0.67 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +5.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.4 | +4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.9 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +4.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.6 | -13.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.6 | -8.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.6 | -9.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.1 | -8.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.2 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:56,836,387-56,914,080 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EFP, RNF147; previously ZNF147 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 34 pathways, smallest: NF-kB activation through FADD/RIP-1 pathway mediated by caspase-8 and -10; TRAF3-dependent IRF activation pathway; TRAF6 mediated IRF7 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14258](https://www.uniprot.org/uniprotkb/Q14258) (E3 ubiquitin/ISG15 ligase TRIM25):

> Functions as a ubiquitin E3 ligase and as an ISG15 E3 ligase. Involved in innate immune defense against viruses by mediating ubiquitination of RIGI and IFIH1. Mediates 'Lys-63'-linked polyubiquitination of the RIGI N-terminal CARD-like region and may play a role in signal transduction that leads to the production of interferons in response to viral infection. Mediates 'Lys-63'-linked polyubiquitination of IFIH1. Promotes ISGylation of 14-3-3 sigma (SFN), an adapter protein implicated in the …

**Summary**, from NCBI Gene [7706](https://www.ncbi.nlm.nih.gov/gene/7706):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein is an RNA binding protein, functions as a ubiquitin E3 ligase and is involved in multiple cellular processes, including regulation of antiviral innate immunity. [provided by RefSeq, Sep 2021]

**Accessions** — [HGNC:12932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12932) · Entrez [7706](https://www.ncbi.nlm.nih.gov/gene/7706) · UniProt [Q14258](https://www.uniprot.org/uniprotkb/Q14258) · Ensembl [ENSG00000121060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121060)

## Data

Gene col 4249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4249); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4249]; `tensor/DDL_lfc|DDL_z.npy` [4249]; `embed/gene_vectors.npy` [4249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4249 or target_col == 4249). Every well: [[TRIM25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ARHGEF10"
type: "gene"
col: 2489
ensembl_id: "ENSG00000104728"
name: "Rho guanine nucleotide exchange factor 10"
location: "8p23.3"
module: 85
arm: "+"
pooled_cpm: 142.45
n_lines_expressing: 42
n_dd_up: 8
n_dd_down: 33
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# ARHGEF10

*Rho guanine nucleotide exchange factor 10* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.39× (z +6.5, q 4e-08, up in 27 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.501× (z -13.3, q 1e-37, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASSF1]] (+0.63, fdr 5e-05), [[SLC17A5]] (+0.61, fdr 2e-05), [[NBEAL1]] (+0.61, fdr 2e-05); moves opposite to [[SOCS6]] (-0.62, fdr 3e-05), [[GTF3C6]] (-0.58, fdr 3e-05), [[RMDN2]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ARFGEF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 4e-08 | 27/40 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +6.0 | 6e-07 | 26/40 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.9 | 7e-07 | 21/40 (LS 180, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.004 | 23/40 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.004 | 20/41 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.004 | 21/41 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.20× | +4.1 | 0.004 | 17/42 (H4, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +4.1 | 0.004 | 19/40 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.004 | 20/40 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.0 | 0.004 | 1/42 (NCI-H1792) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.8 | 0.008 | 16/41 (H4, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.058 | 17/39 (H4, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +3.2 | 0.058 | 17/41 (LS 180, SW1417, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.2 | 0.065 | 11/40 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.085 | 14/40 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.085 | 14/40 (CFPAC-1, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Cepharanthine (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.089 | 10/40 (A-427, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2489.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.501×** | -13.3 | 1e-37 | 32/40 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -12.9 | 1e-35 | 31/41 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.643×** | -12.5 | 2e-33 | 28/40 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.661×** | -11.7 | 2e-29 | 35/40 (C32, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.699×** | -10.1 | 4e-22 | 29/40 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.603×** | -10.1 | 4e-22 | 34/40 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.400×** | -9.6 | 8e-20 | 37/41 (LOX-IMVI, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.644×** | -8.8 | 1e-16 | 35/40 (LOX-IMVI, LoVo, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -8.2 | 1e-14 | 36/40 (LOX-IMVI, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.662×** | -8.2 | 1e-14 | 29/40 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -8.2 | 1e-14 | 33/40 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -7.6 | 1e-12 | 30/39 (Hs 766T, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.664×** | -7.6 | 2e-12 | 28/38 (C-33 A, H4, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.690×** | -7.4 | 5e-12 | 24/40 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -7.2 | 3e-11 | 31/42 (SNU-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -6.9 | 1e-10 | 31/40 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.724×** | -6.5 | 3e-09 | 23/40 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.732×** | -5.9 | 1e-07 | 29/40 (A-172, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.769×** | -5.0 | 2e-05 | 24/39 (BT-474, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 144 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -28.2) |
| [[A-172 (line)]] | wt | 490 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -21.0) |
| [[LoVo (line)]] | wt | 157 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 230 | 0 | 12 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.220× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 216 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -20.5) |
| [[HS-578T (line)]] | alt | 242 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -27.5) |
| [[NCI-H1792 (line)]] | alt | 152 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -17.3) |
| [[Hs 766T (line)]] | wt | 315 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -14.3) |
| [[A498 (line)]] | wt | 198 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -16.3) |
| [[A549 (line)]] | wt | 172 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -23.7) |
| [[COLO 205 (line)]] | alt | 52.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +19.2) | — |
| [[HEC-1-A (line)]] | alt | 244 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -21.4) |
| [[J82 (line)]] | alt | 142 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -16.5) |
| [[H4 (line)]] | wt | 227 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.363× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 174 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +11.7) | [[Harringtonine (drug)]] 5 µM 0.383× (z -11.8) |
| [[SNU-1 (line)]] | wt | 290 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -18.8) |
| [[C-33 A (line)]] | alt | 258 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.4) |
| [[LS 180 (line)]] | wt | 90.8 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 2.13× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 188 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.614× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 81.7 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.15× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.8) |
| [[SW480 (line)]] | alt | 85.2 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.34× (z +11.8) | [[Selinexor (drug)]] 5 µM 0.590× (z -10.5) |
| [[BT-474 (line)]] | alt | 162 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -19.9) |
| [[HOP62 (line)]] | alt | 132 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.313× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 53.5 | 3 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 2.99× (z +9.6) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.79× (z +8.9) | — |
| [[RKO (line)]] | wt | 173 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.367× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -10.3) |
| [[SW48 (line)]] | wt | 186 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.6) |
| [[CHP-212 (line)]] | wt | 138 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.269× (z -12.9) |
| [[SW 1088 (line)]] | alt | 209 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.7) |
| [[SW 900 (line)]] | alt | 136 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | [[Harringtonine (drug)]] 0.5 µM 0.452× (z -8.7) |
| [[SW1417 (line)]] | alt | 56.8 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.81× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.9) |
| [[A-427 (line)]] | wt | 202 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.6) |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF1]] | +0.63 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[SLC17A5]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[NBEAL1]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[KDELR3]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TTC3]] | +0.60 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PTPRF]] | +0.59 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.58 | +0.50 / +0.31 | both halves | 2e-04 |  |
| [[KIAA1328]] | +0.58 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[CLTCL1]] | +0.58 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[ACAP3]] | +0.57 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[STX2]] | +0.57 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[PUSL1]] | +0.57 | +0.49 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS6]] | -0.62 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GTF3C6]] | -0.58 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[RMDN2]] | -0.55 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[DHRS4]] | -0.54 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[NSUN3]] | -0.54 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[CCNT2]] | -0.53 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[KRR1]] | -0.53 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[FAIM]] | -0.53 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[FRS2]] | -0.53 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SMAD1]] | -0.52 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[TOR1A]] | -0.52 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[RBM48]] | -0.52 | -0.40 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARHGEF10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ARHGEF10's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ARHGEF10's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CLTCL1]] | C | CLTCL1 activity raises ARHGEF10's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 5.19× lower at baseline in the lines without CLTCL1 | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARFGEF3]] | B | ARHGEF10 activity lowers ARFGEF3's level | lines that do not express ARHGEF10 (8) vs lines expressing it (42) | 2.34× higher at baseline in the lines without ARHGEF10 | 0.093 | ⚠ within organs, on part of the lines; also absent: LY6E |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (0.8, 7.9); signed map (-40.9, 9.0). **Vector** length 125, 39.4% of its response variance represented; |z| ≥ 3 in 1,371 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.3 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.7 | -11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.3 — chr8:1,823,926-1,958,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0294, Gef10 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 15 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O15013](https://www.uniprot.org/uniprotkb/O15013) (Rho guanine nucleotide exchange factor 10):

> May play a role in developmental myelination of peripheral nerves.

**Summary**, from NCBI Gene [9639](https://www.ncbi.nlm.nih.gov/gene/9639):

> This gene encodes a Rho guanine nucleotide exchange factor (GEF). Rho GEFs regulate the activity of small Rho GTPases by stimulating the exchange of guanine diphosphate (GDP) for guanine triphosphate (GTP) and may play a role in neural morphogenesis. Mutations in this gene are associated with slowed nerve conduction velocity (SNCV). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:14103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14103) · Entrez [9639](https://www.ncbi.nlm.nih.gov/gene/9639) · UniProt [O15013](https://www.uniprot.org/uniprotkb/O15013) · Ensembl [ENSG00000104728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104728)

## Data

Gene col 2489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2489); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2489]; `tensor/DDL_lfc|DDL_z.npy` [2489]; `embed/gene_vectors.npy` [2489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2489 or target_col == 2489). Every well: [[ARHGEF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

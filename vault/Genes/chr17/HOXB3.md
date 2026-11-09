---
symbol: "HOXB3"
type: "gene"
col: 4158
ensembl_id: "ENSG00000120093"
name: "homeobox B3"
location: "17q21.32"
module: 201
arm: "+"
pooled_cpm: 56.59
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 43
n_dd_up_clean: 6
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXB3

*homeobox B3* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +14.4, q 4e-44, up in 30 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.367× (z -18.6, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB6]] (+0.85, fdr 7e-06, ⚠ same locus), [[HOXB5]] (+0.81, fdr 7e-06, ⚠ read-through risk), [[HOXB4]] (+0.79, fdr 7e-06, ⚠ same locus), [[HOXA3]] (+0.69, fdr 1e-05), [[MGST2]] (+0.60, fdr 2e-05), [[TIAL1]] (+0.60, fdr 8e-05); moves opposite to [[SACS]] (-0.58, fdr 1e-05), [[BCL7B]] (-0.53, fdr 3e-05), [[EEFSEC]] (-0.52, fdr 6e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOXB8]] → it (grade B ⚠); 4 go from it, the strongest it → [[PTPRG-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +14.4 | 4e-44 | 30/39 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.22×** | +5.2 | 7e-05 | 17/39 (SW480, NCI-H1792, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +5.0 | 9e-05 | 16/38 (LoVo, LS 180, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 18/39 (PANC-1, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.003 | 12/38 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.005 | 12/38 (PANC-1, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.015 | 16/38 (A-172, KATO III, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.015 | 13/39 (LoVo, HCT15, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.061 | 8/38 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.068 | 15/38 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.068 | 9/39 (AsPC-1, SW48, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | 1.37× | +3.0 | 0.10 | 9/38 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.10 | 9/39 (AsPC-1, SW48, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.367×** | -18.6 | 0e+00 | 37/39 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.409×** | -16.6 | 0e+00 | 39/39 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -14.8 | 0e+00 | 34/38 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.602×** | -13.3 | 2e-38 | 29/39 (A-172, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.502×** | -12.8 | 1e-35 | 26/39 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.510×** | -12.5 | 5e-34 | 35/38 (SW480, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.500×** | -12.4 | 2e-33 | 29/39 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.524×** | -12.0 | 2e-31 | 34/38 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -11.7 | 5e-30 | 27/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.523×** | -11.6 | 2e-29 | 32/38 (SHP-77, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -10.9 | 6e-26 | 34/38 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -10.9 | 9e-26 | 26/38 (AN3 CA, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.549×** | -10.3 | 2e-23 | 27/35 (LoVo, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.609×** | -9.2 | 1e-18 | 25/36 (LoVo, C32, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.619×** | -8.9 | 2e-17 | 23/38 (SHP-77, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -8.9 | 3e-17 | 30/38 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.671×** | -7.0 | 7e-11 | 28/39 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -6.1 | 3e-08 | 23/39 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.712×** | -6.1 | 4e-08 | 20/39 (PANC-1, HCT15, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.735×** | -5.7 | 2e-07 | 19/38 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.753×** | -5.3 | 3e-06 | 19/38 (LoVo, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.829×** | -4.9 | 2e-05 | 19/39 (PANC-1, NCI-H661, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 169 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0833× (z -31.2) |
| [[HT-29 (line)]] | alt | 165 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -20.6) |
| [[PANC-1 (line)]] | alt | 160 | 1 | 11 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.175× (z -21.6) |
| [[C32 (line)]] | wt | 37.7 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -13.6) |
| [[LoVo (line)]] | wt | 99.7 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -11.7) |
| [[SHP-77 (line)]] | alt | 43.6 | 2 | 6 (3 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.46× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -15.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.147× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 36.7 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.201× (z -9.8) |
| [[SW1417 (line)]] | alt | 192 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.51× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -17.5) |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.236× (z -11.2) |
| [[A-172 (line)]] | wt | 92.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -20.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 44.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -16.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.323× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 75.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0917× (z -15.9) |
| [[A498 (line)]] | wt | 39.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -17.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.214× (z -15.2) |
| [[HCT15 (line)]] | alt | 203 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.151× (z -13.9) |
| [[COLO 205 (line)]] | alt | 59.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.126× (z -13.5) |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.316× (z -8.9) |
| [[Hs 766T (line)]] | wt | 44.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.200× (z -13.0) |
| [[SW48 (line)]] | wt | 112 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0514× (z -11.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.263× (z -9.5) |
| [[AN3 CA (line)]] | alt | 45.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0407× (z -14.8) |
| [[KATO III (line)]] | alt | 52.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.281× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 36.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.359× (z -9.4) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0675× (z -9.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -8.8) |
| [[A-427 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 9 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB6]] | +0.85 | +0.81 / +0.83 | both halves | 7e-06 | same gene group; STRING 836; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB5]] | +0.81 | +0.83 / +0.75 | both halves | 7e-06 | same gene group; STRING 874; ⚠ **readthrough risk**: HOXB5 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[HOXB4]] | +0.79 | +0.66 / +0.77 | both halves | 7e-06 | same gene group; pathway: Activation of HOX genes during differentiation; STRING 887; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB-AS3]] | +0.77 | +0.73 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXA3]] | +0.69 | +0.55 / +0.65 | both halves | 1e-05 | same gene group; pathway: Activation of HOX genes during differentiation; STRING 412 |
| [[HOXB8]] | +0.64 | +0.52 / +0.53 | both halves | 1e-05 | same gene group; STRING 714; ⚠ same locus (6.5 kb, same strand: neighbours can correlate without regulation) |
| [[MGST2]] | +0.60 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TIAL1]] | +0.60 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[HOXB7]] | +0.59 | +0.46 / +0.50 | both halves | 2e-05 | same gene group; STRING 547; ⚠ same locus (2.3 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF821]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[GPBP1L1]] | +0.56 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[HOXC9]] | +0.56 | +0.30 / +0.52 | both halves | 2e-04 | same gene group |
| [[TSC22D4]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CDC14A]] | +0.56 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ZNF224]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[IST1]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[GPRC5C]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[P4HTM]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SACS]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[BCL7B]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.52 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[SUPT3H]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 | same gene group |
| [[TMEM185B]] | -0.50 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TAF1B]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[IQCH]] | -0.49 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[DTD1]] | -0.49 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[TTPAL]] | -0.49 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[CIAO1]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[HLCS]] | -0.48 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[NEK1]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB8]] | B | HOXB8 activity raises HOXB3's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 3.26× lower at baseline in the lines without HOXB8 | 0.011 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C |
| [[HOXB4]] | B | HOXB4 activity raises HOXB3's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 3.54× lower at baseline in the lines without HOXB4 | 0.057 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXB5]], [[HOXB6]] | C | HOXB5, HOXB6 activity raises HOXB3's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 4.32× lower at baseline in the lines without HOXB5, HOXB6 | 0.008 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent with the target; co-absent genes |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRG-AS1]] | B | HOXB3 activity lowers PTPRG-AS1's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 1.64× higher at baseline in the lines without HOXB3 | 0.081 | ⚠ within organs, on part of the lines; also absent: HOXB6 |
| [[TAF1B]] | B | HOXB3 activity lowers TAF1B's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 1.27× higher at baseline in the lines without HOXB3 | 0.090 | ⚠ within organs, on part of the lines; also absent: HOXB6 |
| [[HOXB6]] | C | HOXB3 activity raises HOXB6's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 4.73× lower at baseline in the lines without HOXB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: HOXB6; co-absent with the target |
| [[HOXB5]] | C | HOXB3 activity raises HOXB5's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 3.36× lower at baseline in the lines without HOXB3 | 0.024 | ⚠ within organs, on part of the lines; also absent: HOXB6; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.1, 26.8); signed map (39.2, -4.1). **Vector** length 93.1, 23.4% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Kidney development* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +14.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.9 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -0.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.6 | -18.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.6 | -16.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.8 | -12.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -10.9 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,548,870-48,604,912 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2, HOX2G |
| Gene groups (HGNC) | HOXL subclass homeoboxes; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P14651](https://www.uniprot.org/uniprotkb/P14651) (Homeobox protein Hox-B3):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3213](https://www.ncbi.nlm.nih.gov/gene/3213):

> This gene is a member of the Antp homeobox family and encodes a nuclear protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded protein functions as a sequence-specific transcription factor that is involved in development. Increased expression of this gene is associated with a distinct biologic subset of acute myeloid leukemia (AML). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5114) · Entrez [3213](https://www.ncbi.nlm.nih.gov/gene/3213) · UniProt [P14651](https://www.uniprot.org/uniprotkb/P14651) · Ensembl [ENSG00000120093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120093)

## Data

Gene col 4158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4158); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4158]; `tensor/DDL_lfc|DDL_z.npy` [4158]; `embed/gene_vectors.npy` [4158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4158 or target_col == 4158). Every well: [[HOXB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

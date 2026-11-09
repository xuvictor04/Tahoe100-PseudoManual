---
symbol: "DBN1"
type: "gene"
col: 3500
ensembl_id: "ENSG00000113758"
name: "drebrin 1"
location: "5q35.3"
module: 25
arm: "+"
pooled_cpm: 30.15
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DBN1

*drebrin 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +13.4, q 2e-38, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.74× (z +4.8, q 2e-04, up in 25 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.634× (z -5.5, q 2e-05, down in 35 of 45 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.701× (z -4.3, q 0.002, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC2]] (+0.79, fdr 7e-06), [[SCRIB]] (+0.67, fdr 7e-06), [[SGPL1]] (+0.66, fdr 2e-05); moves opposite to [[TRIM7-AS2]] (-0.60, fdr 3e-05), [[TMEM258]] (-0.59, fdr 2e-05), [[SMIM27]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC4A3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FLNA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +13.4 | 2e-38 | 42/43 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +12.3 | 2e-32 | 34/38 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +11.6 | 5e-29 | 38/43 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +8.2 | 3e-14 | 27/45 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +5.1 | 4e-05 | 27/43 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.74×** | +4.8 | 2e-04 | 25/45 (HT-29, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.6 | 4e-04 | 21/45 (SNU-423, SW480, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +4.5 | 5e-04 | 20/45 (HT-29, NCI-H460, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.4 | 6e-04 | 21/44 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.45×** | +4.3 | 9e-04 | 27/44 (A498, BT-474, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +4.3 | 1e-03 | 26/44 (HT-29, NCI-H460, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.96×** | +4.2 | 0.001 | 25/43 (HT-29, SW480, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.001 | 24/45 (PANC-1, SNU-423, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.002 | 18/45 (NCI-H460, BT-474, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.002 | 21/44 (H4, NCI-H460, …) | all doses, flat | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.008 | 17/45 (NCI-H2347, SHP-77, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.010 | 19/44 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.013 | 16/45 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Voriconazole (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.015 | 16/45 (NCI-H460, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.015 | 19/44 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.017 | 17/44 (NCI-H23, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.045 | 15/45 (HT-29, KATO III, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.052 | 15/44 (LOX-IMVI, BT-474, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.634×** | -5.5 | 2e-05 | 35/45 (NCI-H2030, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.652×** | -5.2 | 6e-05 | 25/45 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.674×** | -4.8 | 3e-04 | 23/45 (SK-MEL-2, A-427, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.701×** | -4.3 | 0.002 | 28/45 (RKO, SW1417, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.701×** | -4.3 | 0.002 | 28/45 (RKO, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.729×** | -3.8 | 0.011 | 22/45 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.736×** | -3.6 | 0.027 | 20/44 (SW 900, SW48, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.822×** | -3.4 | 0.042 | 26/45 (RKO, HOP62, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.042 | 16/45 (HOP62, Panc 03.27, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.823×** | -3.4 | 0.042 | 17/45 (Hs 766T, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.733×** | -3.4 | 0.042 | 13/45 (PANC-1, RKO, …) | two highest doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.065 | 21/45 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -3.2 | 0.066 | 8/45 (LoVo, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.780× | -3.0 | 0.10 | 21/44 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 29.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.05× (z +12.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 40.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 26.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 26.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 25.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.04× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 26.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 36.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.88× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.55× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 31.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 45.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0523× (z -12.4) |
| [[HOP62 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.38× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 45.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.19× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.45× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC2]] | +0.79 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[SCRIB]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SGPL1]] | +0.66 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[MYH9]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 | STRING 405 |
| [[EIF4H]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[FLNA]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 | STRING 612 |
| [[DCTN1]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[PDAP1]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HUWE1]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.64 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[CEP170B]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[NONO]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM7-AS2]] | -0.60 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SMIM27]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[DPM3]] | -0.59 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[NDUFA7]] | -0.59 | -0.37 / -0.66 | both halves | 8e-05 |  |
| [[CHCHD1]] | -0.58 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[DDT]] | -0.58 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[LAMTOR5]] | -0.58 | -0.39 / -0.65 | both halves | 6e-05 |  |
| [[COX6B1]] | -0.58 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[MINCR]] | -0.57 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[ABHD18]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises DBN1's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without SLC4A3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[TOP2A]] | B | TOP2A activity raises DBN1's level | compounds that target TOP2A: 3 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLNA]] | C | DBN1 activity raises FLNA's level | lines that do not express DBN1 (3) vs lines expressing it (47) | 3.56× lower at baseline in the lines without DBN1 | 0.009 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: LTBP3, NUAK1, BLVRA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.589). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-33.4, -20.3); signed map (-14.7, -37.2). **Vector** length 109, 28.5% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +13.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.2 | +5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +0.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.4 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -3.0 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.4 | -5.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.9 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -4.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.5 | +0.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | drebrin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,456,608-177,474,401 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously D0S117E |
| Gene groups (HGNC) | Drebrin family |
| Reactome | 8 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle; RHOH GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16643](https://www.uniprot.org/uniprotkb/Q16643) (Drebrin):

> Actin cytoskeleton-organizing protein that plays a role in the formation of cell projections. Required for actin polymerization at immunological synapses (IS) and for the recruitment of the chemokine receptor CXCR4 to IS. Plays a role in dendritic spine morphogenesis and organization, including the localization of the dopamine receptor DRD1 to the dendritic spines (By similarity). Involved in memory-related synaptic plasticity in the hippocampus (By similarity).

**Summary**, from NCBI Gene [1627](https://www.ncbi.nlm.nih.gov/gene/1627):

> The protein encoded by this gene is a cytoplasmic actin-binding protein thought to play a role in the process of neuronal growth. It is a member of the drebrin family of proteins that are developmentally regulated in the brain. A decrease in the amount of this protein in the brain has been implicated as a possible contributing factor in the pathogenesis of memory disturbance in Alzheimer's disease. At least two alternative splice variants encoding different protein isoforms have been described …

**Accessions** — [HGNC:2695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2695) · Entrez [1627](https://www.ncbi.nlm.nih.gov/gene/1627) · UniProt [Q16643](https://www.uniprot.org/uniprotkb/Q16643) · Ensembl [ENSG00000113758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113758)

## Data

Gene col 3500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3500); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3500]; `tensor/DDL_lfc|DDL_z.npy` [3500]; `embed/gene_vectors.npy` [3500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3500 or target_col == 3500). Every well: [[DBN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

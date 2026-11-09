---
symbol: "ASNS"
type: "gene"
col: 959
ensembl_id: "ENSG00000070669"
name: "asparagine synthetase (glutamine-hydrolyzing)"
location: "7q21.3"
module: 63
arm: "+"
pooled_cpm: 85.16
n_lines_expressing: 46
n_dd_up: 41
n_dd_down: 24
n_dd_up_clean: 38
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ASNS

*asparagine synthetase (glutamine-hydrolyzing)* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (3 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 2.29× (z +15.2, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.361× (z -13.2, q 5e-37, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHGDH]] (+0.90, fdr 7e-06), [[AARS1]] (+0.89, fdr 7e-06), [[MTHFD2]] (+0.89, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CHAC1]] → it (grade B ⚠); 3 go from it, the strongest it → [[CEBPG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **2.29×** | +15.2 | 0e+00 | 41/44 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.70×** | +12.8 | 4e-35 | 44/44 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.96×** | +12.3 | 1e-32 | 40/44 (SW480, C-33 A, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.44×** | +11.5 | 2e-28 | 41/44 (NCI-H2347, AsPC-1, …) | all doses, flat | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **2.25×** | +10.5 | 1e-23 | 40/44 (SNU-1, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +10.2 | 2e-22 | 34/43 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.99×** | +8.9 | 5e-17 | 36/44 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.86×** | +8.0 | 7e-14 | 32/44 (C-33 A, LOX-IMVI, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.52×** | +7.7 | 1e-12 | 33/45 (SNU-1, Hs 766T, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.79×** | +7.5 | 3e-12 | 34/44 (SHP-77, AsPC-1, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.72×** | +7.0 | 1e-10 | 35/43 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +6.2 | 2e-08 | 27/44 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +5.9 | 2e-07 | 29/45 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.57×** | +5.8 | 3e-07 | 28/44 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +5.7 | 4e-07 | 27/44 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.54×** | +5.6 | 9e-07 | 28/44 (SHP-77, BT-474, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.28×** | +5.6 | 9e-07 | 27/44 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.361×** | -13.2 | 5e-37 | 40/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.380×** | -12.0 | 6e-31 | 37/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.550×** | -10.9 | 2e-25 | 31/44 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.458×** | -9.3 | 1e-18 | 38/43 (LoVo, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.507×** | -7.8 | 7e-13 | 28/44 (SW48, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -6.0 | 1e-07 | 25/44 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.661×** | -5.4 | 7e-06 | 30/44 (NCI-H23, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.748×** | -5.3 | 7e-06 | 29/44 (PANC-1, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -5.3 | 9e-06 | 24/44 (H4, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **0.754×** | -5.2 | 1e-05 | 28/44 (KATO III, LoVo, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.639×** | -5.1 | 1e-05 | 29/45 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.679×** | -5.0 | 2e-05 | 29/44 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -4.1 | 0.001 | 22/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.559×** | -3.9 | 0.003 | 22/45 (H4, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.003 | 21/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.808×** | -3.9 | 0.003 | 21/44 (A-427, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 252 | 0 | 13 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0745× (z -18.7) |
| [[PANC-1 (line)]] | alt | 254 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -31.4) |
| [[SW480 (line)]] | alt | 116 | 7 (1 ⚠) | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +12.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.321× (z -12.9) |
| [[H4 (line)]] | wt | 186 | 1 | 10 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.73× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -19.7) |
| [[HT-29 (line)]] | alt | 246 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -22.0) |
| [[SW1417 (line)]] | alt | 106 | 1 (1 ⚠) | 10 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.29× (z +10.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.3) |
| [[SW48 (line)]] | wt | 271 | 2 | 9 (2 ⚠) | [[Artesunate (drug)]] 5 µM 2.58× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -17.4) |
| [[A-172 (line)]] | wt | 36.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.5) |
| [[A-427 (line)]] | wt | 109 | 1 | 5 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.94× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -31.3) |
| [[LoVo (line)]] | wt | 177 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0748× (z -23.3) |
| [[A498 (line)]] | wt | 106 | 1 (1 ⚠) | 4 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.77× (z +9.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -13.9) |
| [[C-33 A (line)]] | alt | 63.0 | 4 (1 ⚠) | 1 | [[5-Azacytidine (drug)]] 5 µM 5.59× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 28.1 | 5 (2 ⚠) | 0 | [[5-Azacytidine (drug)]] 5 µM 5.89× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 116 | 4 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.37× (z +13.4) | [[Harringtonine (drug)]] 0.05 µM 0.132× (z -12.0) |
| [[RKO (line)]] | wt | 152 | 1 | 3 | [[Artesunate (drug)]] 5 µM 2.69× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 53.4 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.44× (z +11.5) ⚠ unreliable plate only · without an alert: [[5-Azacytidine (drug)]] 5 µM 3.96× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 33.8 | 3 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 5.55× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 105 | 1 | 2 | [[Artesunate (drug)]] 5 µM 2.88× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.172× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 64.9 | 3 | 0 | [[Artesunate (drug)]] 5 µM 3.32× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 41.0 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.11× (z +12.5) ⚠ unreliable plate only | [[Harringtonine (drug)]] 0.5 µM 0.270× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 45.4 | 3 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.01× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 32.9 | 3 | 0 | [[Artesunate (drug)]] 5 µM 3.31× (z +10.5) | — |
| [[A549 (line)]] | wt | 27.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change · without an alert: [[Artesunate (drug)]] 5 µM 2.95× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 216 | 2 | 0 | [[Artesunate (drug)]] 5 µM 3.59× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 93.2 | 2 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.89× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 32.7 | 1 | 0 | [[Artesunate (drug)]] 5 µM 3.61× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 37.1 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.255× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 45.6 | 1 | 0 | [[Artesunate (drug)]] 5 µM 3.31× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 52.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.1) |
| [[HS-578T (line)]] | alt | 68.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 62.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.1) |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 34.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.4) |
| [[SW 900 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.83× (z +9.4) ⚠ unreliable plate only | — |
| [[AN3 CA (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHGDH]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 829 |
| [[AARS1]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 | STRING 840 |
| [[MTHFD2]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 717 |
| [[PSAT1]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 864 |
| [[GARS1]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | STRING 850 |
| [[CHAC1]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 807 |
| [[CARS1]] | +0.88 | +0.92 / +0.84 | both halves | 7e-06 | STRING 536 |
| [[MARS1]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 653 |
| [[SARS1]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 500 |
| [[IARS1]] | +0.83 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 804 |
| [[XPOT]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[GOT1]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 969 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHAC1]] | B | CHAC1 activity raises ASNS's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 3.01× lower at baseline in the lines without CHAC1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[ASNSP1]] | B | ASNSP1 activity raises ASNS's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.67× lower at baseline in the lines without ASNSP1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[CTH]] | B | CTH activity raises ASNS's level | lines that do not express CTH (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without CTH | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises ASNS's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 4.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANK2]] | B | ANK2 activity raises ASNS's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.27× lower at baseline in the lines without ANK2 | 0.086 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[LINC00662]] | C | LINC00662 activity lowers ASNS's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 4.12× higher at baseline in the lines without LINC00662 | 0.033 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEBPG]] | C | ASNS's natural level weakens CEBPG's drug response | ASNS's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.42; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[GARS1]] | C | ASNS activity raises GARS1's level | lines that do not express ASNS (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without ASNS | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PPEF1; maybe low, not absent; its own permutation p |
| [[HSPA9]] | C | ASNS activity raises HSPA9's level | lines that do not express ASNS (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without ASNS | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PPEF1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.925). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 48.0); signed map (-13.5, 24.5). **Vector** length 166, 59.8% of its response variance represented; |z| ≥ 3 in 1,608 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.82 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.82 to 9); *Amino acid transport across the plasma membrane* (reactome, mean cos +0.72 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +11.5 | +15.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +9.8 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.4 | +11.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +8.7 | +10.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.5 | +12.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.4 | +7.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +6.9 | +7.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.5 | -12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -13.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -7.4 | -9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -5.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.9 | -5.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -4.3 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | asparagine synthetase (glutamine-hydrolyzing) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:97,851,677-97,872,542 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Asparagine synthase family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, UV_RESPONSE_UP, HEME_METABOLISM, MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: Aspartate and asparagine metabolism; Response of EIF2AK1 (HRI) to heme deficiency; ATF4 activates genes in response to endoplasmic reticulum  stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P08243](https://www.uniprot.org/uniprotkb/P08243) (Asparagine synthetase):

> Catalyzes the ATP-dependent synthesis of L-asparagine from L-aspartate, using L-glutamine as a source of nitrogen. Can also use ammonia as the nitrogen source in vitro.

**Summary**, from NCBI Gene [440](https://www.ncbi.nlm.nih.gov/gene/440):

> The protein encoded by this gene is involved in the synthesis of asparagine. This gene complements a mutation in the temperature-sensitive hamster mutant ts11, which blocks progression through the G1 phase of the cell cycle at nonpermissive temperature. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:753) · Entrez [440](https://www.ncbi.nlm.nih.gov/gene/440) · UniProt [P08243](https://www.uniprot.org/uniprotkb/P08243) · Ensembl [ENSG00000070669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070669)

## Data

Gene col 959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 959); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 959]; `tensor/DDL_lfc|DDL_z.npy` [959]; `embed/gene_vectors.npy` [959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 959 or target_col == 959). Every well: [[ASNS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASNS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

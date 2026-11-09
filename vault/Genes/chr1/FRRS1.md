---
symbol: "FRRS1"
type: "gene"
col: 8020
ensembl_id: "ENSG00000156869"
name: "ferric chelate reductase 1"
location: "1p21.2"
module: 45
arm: "+"
pooled_cpm: 22.13
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# FRRS1

*ferric chelate reductase 1* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +7.4, q 9e-11, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.399× (z -13.2, q 6e-37, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIP4P2]] (+0.64, fdr 7e-06), [[TMEM14A]] (+0.63, fdr 1e-05), [[FAM229B]] (+0.62, fdr 1e-05); moves opposite to [[CDR2]] (-0.62, fdr 1e-05), [[MFSD14CP-1]] (-0.59, fdr 1e-05), [[ENOX2]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CAT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.4 | 9e-11 | 35/45 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +6.9 | 2e-09 | 33/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +6.4 | 3e-08 | 32/44 (A498, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +5.7 | 2e-06 | 21/45 (A-427, SW48, …) | rises with dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 4e-04 | 18/45 (MIA PaCa-2, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 0.002 | 16/45 (LoVo, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.1 | 0.004 | 17/43 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +3.9 | 0.006 | 19/45 (A498, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +3.6 | 0.018 | 18/45 (NCI-H1573, A498, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.044 | 15/42 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.1 | 0.085 | 11/45 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.12 | 10/44 (A498, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8020.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.399×** | -13.2 | 6e-37 | 39/45 (HCT15, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -8.7 | 9e-16 | 32/43 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -7.7 | 3e-12 | 26/40 (SW480, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -6.6 | 6e-09 | 20/29 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.648×** | -6.2 | 5e-08 | 23/35 (HCT15, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -6.2 | 6e-08 | 27/42 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.577×** | -5.6 | 1e-06 | 26/43 (AsPC-1, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.697×** | -5.2 | 1e-05 | 26/44 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.688×** | -5.2 | 1e-05 | 24/44 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -5.1 | 2e-05 | 23/43 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.694×** | -4.9 | 6e-05 | 18/34 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.807×** | -4.4 | 5e-04 | 19/45 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.771×** | -3.8 | 0.008 | 18/44 (CFPAC-1, H4, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.778×** | -3.6 | 0.012 | 15/45 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.782×** | -3.6 | 0.013 | 18/43 (NCI-H1792, HCT15, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.013 | 17/44 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.016 | 15/43 (NCI-H1573, H4, …) | two highest doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.795×** | -3.3 | 0.028 | 9/45 (SW 1088, H4, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.725×** | -3.3 | 0.028 | 14/42 (COLO 205, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.860× | -3.1 | 0.055 | 11/45 (HS-578T, LoVo, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.671×** | -3.0 | 0.072 | 13/40 (NCI-H460, NCI-H23, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 42.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0960× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.125× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 66.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 21.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.234× (z -12.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -12.1) |
| [[C32 (line)]] | wt | 28.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.160× (z -12.1) |
| [[H4 (line)]] | wt | 26.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.150× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 45.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0957× (z -17.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.78 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.190× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.184× (z -9.4) |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -14.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -9.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 16.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.236× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.306× (z -8.8) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 23.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.4) |
| [[RKO (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.206× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -9.1) |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.121× (z -9.0) |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0957× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP4P2]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TMEM14A]] | +0.63 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[FAM229B]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RADX]] | +0.60 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[GPR160]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FHIP1A]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[PGAP1]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[VWDE]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[WDR17]] | +0.59 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[TM7SF3]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PEX2]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[SNX2]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDR2]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | -0.59 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.58 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[DOCK1]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ANKMY1]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[AVEN]] | -0.56 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[ANKLE2]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PHF2]] | -0.55 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[NPIPB4]] | -0.55 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[NUTM2B-AS1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SOGA1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SEMA6A-AS1]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FRRS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FHIP1A]] | B | FHIP1A activity raises FRRS1's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without FHIP1A | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAT]] | C | FRRS1 activity lowers CAT's level | lines that do not express FRRS1 (3) vs lines expressing it (47) | 2.90× higher at baseline in the lines without FRRS1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGEF10L, WDR49, CPT1B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.9, -8.7); signed map (-28.6, -7.9). **Vector** length 102, 24.2% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.4 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.1 | -13.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -5.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.4 | -2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.3 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ferric chelate reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:99,703,970-99,766,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR2; previously SDFR2 |
| Gene groups (HGNC) | Cytochrome b561; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNA5](https://www.uniprot.org/uniprotkb/Q6ZNA5) (Ferric reductase 1):

> Ferric reductase that reduces Fe(3+) to Fe(2+) and could play a role in iron import into cells (By similarity). The electron donor and therefore the reaction mechanism are not known (By similarity).

**Summary**, from NCBI Gene [391059](https://www.ncbi.nlm.nih.gov/gene/391059):

> Members of the cytochrome b561 (CYB561; MIM 600019) family, including FRRS1, reduce ferric to ferrous iron before its transport from the endosome to the cytoplasm (Vargas et al., 2003 [PubMed 14499595]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:27622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27622) · Entrez [391059](https://www.ncbi.nlm.nih.gov/gene/391059) · UniProt [Q6ZNA5](https://www.uniprot.org/uniprotkb/Q6ZNA5) · Ensembl [ENSG00000156869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156869)

## Data

Gene col 8020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8020); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8020]; `tensor/DDL_lfc|DDL_z.npy` [8020]; `embed/gene_vectors.npy` [8020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8020 or target_col == 8020). Every well: [[FRRS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRRS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

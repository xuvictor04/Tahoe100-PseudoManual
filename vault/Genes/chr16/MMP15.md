---
symbol: "MMP15"
type: "gene"
col: 2300
ensembl_id: "ENSG00000102996"
name: "matrix metallopeptidase 15"
location: "16q21"
module: 176
arm: "+"
pooled_cpm: 7.25
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# MMP15

*matrix metallopeptidase 15* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.44× (z +14.2, q 6e-43, up in 31 of 41 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.05× (z +11.6, q 4e-29, up in 28 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.344× (z -12.2, q 1e-31, down in 27 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.381× (z -11.1, q 5e-26, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYAL2]] (+0.65, fdr 1e-05), [[JAG2]] (+0.63, fdr 1e-05), [[PODXL2]] (+0.63, fdr 1e-05); moves opposite to [[N4BP2L2]] (-0.58, fdr 2e-05), [[GTF2IRD2]] (-0.56, fdr 3e-05), [[ENTPD3-AS1]] (-0.56, fdr 3e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[HES2]] → it (grade B ⚠); 8 go from it, the strongest it → [[EPHB4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.44×** | +14.2 | 6e-43 | 31/41 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.30×** | +13.7 | 3e-40 | 28/41 (NCI-H460, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.06×** | +12.9 | 1e-35 | 31/41 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +11.6 | 4e-29 | 28/40 (NCI-H460, NCI-H2030, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +11.6 | 5e-29 | 25/35 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.61×** | +11.0 | 3e-26 | 32/41 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.20×** | +9.0 | 1e-17 | 21/28 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.82×** | +6.8 | 5e-10 | 22/38 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +6.7 | 1e-09 | 26/40 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.80×** | +6.2 | 3e-08 | 17/39 (NCI-H2030, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.73×** | +6.1 | 7e-08 | 6/13 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.58×** | +5.0 | 2e-05 | 16/34 (A498, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.54×** | +4.8 | 9e-05 | 13/36 (LS 180, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.7 | 1e-04 | 9/30 (CFPAC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.5 | 2e-04 | 13/40 (Panc 03.27, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.016 | 10/40 (A498, HOP62, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.021 | 9/40 (HT-29, KATO III, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.028 | 1/35 (A549) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.066 | 6/41 (A498, NCI-H2347, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.068 | 1/26 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +2.9 | 0.076 | 8/40 (A549, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.344×** | -12.2 | 1e-31 | 27/36 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -11.1 | 5e-26 | 32/41 (SW48, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -10.4 | 7e-23 | 29/40 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.501×** | -7.6 | 4e-12 | 24/39 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.548×** | -6.9 | 6e-10 | 19/40 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.548×** | -6.7 | 2e-09 | 22/35 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.576×** | -6.1 | 9e-08 | 23/39 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.688×** | -6.1 | 9e-08 | 23/35 (NCI-H2347, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -6.0 | 1e-07 | 21/40 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -4.8 | 1e-04 | 20/40 (LS 180, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -4.3 | 8e-04 | 13/40 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -4.2 | 0.001 | 13/40 (HT-29, KATO III, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -3.8 | 0.006 | 13/39 (LoVo, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.749×** | -3.1 | 0.072 | 12/38 (HepG2/C3A, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.763×** | -3.1 | 0.072 | 3/41 (HS-578T, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 10.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0597× (z -15.0) |
| [[SW48 (line)]] | wt | 13.0 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0376× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 6.39 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.106× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.0) |
| [[J82 (line)]] | alt | 5.49 | 0 | 2 (2 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.104× (z -8.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 17.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.222× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -10.5) |
| [[A498 (line)]] | wt | 5.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.5) | — |
| [[A549 (line)]] | wt | 4.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 9.80 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0765× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.163× (z -10.0) |
| [[KATO III (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -9.4) |
| [[LoVo (line)]] | wt | 15.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +10.6) | — |
| [[SW480 (line)]] | alt | 4.25 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0390× (z -16.6) |
| [[A-172 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYAL2]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[JAG2]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.63 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[EPHB4]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CORO2A]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SEPTIN3]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.59 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GPC4]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CELSR2]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.57 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[B3GNT2]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2L2]] | -0.58 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[GTF2IRD2]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ENTPD3-AS1]] | -0.56 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.56 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.55 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[VPS45]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[HEXIM2-AS1]] | -0.54 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ANKRD17-DT]] | -0.54 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[C15orf40]] | -0.54 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[FCF1]] | -0.53 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[NEK11]] | -0.53 | -0.37 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES2]] | B | HES2 activity raises MMP15's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without HES2 | 0.008 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[P2RY2]] | B | P2RY2 activity raises MMP15's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without P2RY2 | 0.008 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[LAMA5]] | B | LAMA5 activity raises MMP15's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without LAMA5 | 0.026 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises MMP15's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without MCF2L | 0.029 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[ENTPD2]] | B | ENTPD2 activity raises MMP15's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without ENTPD2 | 0.031 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[CELSR2]] | B | CELSR2 activity raises MMP15's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.10× lower at baseline in the lines without CELSR2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[LINC02100]] | B | LINC02100 activity lowers MMP15's level | lines that do not express LINC02100 (9) vs lines expressing it (41) | 2.15× higher at baseline in the lines without LINC02100 | 0.048 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, RASA3 |
| [[EPHA1]] | B | EPHA1 activity raises MMP15's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without EPHA1 | 0.054 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[BMP8B]] | B | BMP8B activity raises MMP15's level | lines that do not express BMP8B (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without BMP8B | 0.073 | ⚠ within organs, on part of the lines; also absent: PBX4, SPECC1, CTSV; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises MMP15's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without JAG2 | 0.073 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB4]] | B | MMP15 activity raises EPHB4's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without MMP15 | 0.022 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[EFNA4]] | B | MMP15 activity raises EFNA4's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without MMP15 | 0.033 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[LAMA5]] | B | MMP15 activity raises LAMA5's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 3.67× lower at baseline in the lines without MMP15 | 0.036 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[CORO2A]] | B | MMP15 activity strengthens CORO2A's drug response | lines that do not express MMP15 (6) vs lines expressing it (39) | the lines without MMP15 respond 0.51× as strongly (z diff +2.60); strongest at Harringtonine 5 µM: 0.99x vs 0.32x (z diff +5.5) | 0.041 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PDZD4]] | B | MMP15 activity raises PDZD4's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without MMP15 | 0.064 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[TSPAN14]] | B | MMP15 activity raises TSPAN14's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without MMP15 | 0.066 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[HES2]] | B | MMP15 activity raises HES2's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without MMP15 | 0.072 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[FGFR3]] | B | MMP15 activity raises FGFR3's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without MMP15 | 0.086 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.3, 29.9); signed map (-22.7, 34.1). **Vector** length 72.9, 13.5% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +3.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.5 | +9.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.1 | +13.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +6.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.5 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,025,754-58,046,901 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MT2-MMP, MTMMP2, SMCP-2 |
| Gene groups (HGNC) | M10 matrix metallopeptidases |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Reactome | 4 pathways, smallest: Activation of Matrix Metalloproteinases; Collagen degradation; Degradation of the extracellular matrix |
| Matched by | ensembl_id |

**Function**, from UniProt [P51511](https://www.uniprot.org/uniprotkb/P51511) (Matrix metalloproteinase-15):

> Endopeptidase that degrades various components of the extracellular matrix. May activate progelatinase A.

**Summary**, from NCBI Gene [4324](https://www.ncbi.nlm.nih.gov/gene/4324):

> This gene encodes a member of the peptidase M10 family and membrane-type subfamily of matrix metalloproteinases (MMPs). Proteins in this family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. Members of this subfamily contain a transmembrane domain suggesting that these proteins are expressed at the cell surface rather …

**Accessions** — [HGNC:7161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7161) · Entrez [4324](https://www.ncbi.nlm.nih.gov/gene/4324) · UniProt [P51511](https://www.uniprot.org/uniprotkb/P51511) · Ensembl [ENSG00000102996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102996)

## Data

Gene col 2300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2300); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2300]; `tensor/DDL_lfc|DDL_z.npy` [2300]; `embed/gene_vectors.npy` [2300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2300 or target_col == 2300). Every well: [[MMP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

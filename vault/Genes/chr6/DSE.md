---
symbol: "DSE"
type: "gene"
col: 3287
ensembl_id: "ENSG00000111817"
name: "dermatan sulfate epimerase"
location: "6q22.1"
module: 112
arm: "+"
pooled_cpm: 53.64
n_lines_expressing: 41
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 14
direction_downstream: 3
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# DSE

*dermatan sulfate epimerase* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +31.9, q 0e+00, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Medroxyprogesterone acetate (drug)]] 0.5 µM: 0.766× (z -6.5, q 5e-08, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01828]] (+0.67, fdr 1e-05), [[HMGN2P46]] (+0.67, fdr 7e-06), [[GATM]] (+0.62, fdr 1e-05); moves opposite to [[WDR5]] (-0.55, fdr 4e-05), [[PYGB]] (-0.54, fdr 2e-05), [[NUP160]] (-0.52, fdr 7e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MIR155HG]] → it (grade B ⚠); 3 go from it, the strongest it → [[AKT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +31.9 | 0e+00 | 32/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +21.3 | 0e+00 | 27/39 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +11.1 | 2e-26 | 19/39 (A-427, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +10.6 | 6e-24 | 23/39 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +10.2 | 3e-22 | 25/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +10.2 | 3e-22 | 23/39 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +7.9 | 2e-13 | 18/39 (A-172, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.2 | 3e-11 | 17/39 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +5.0 | 3e-05 | 16/40 (HOP62, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.9 | 6e-05 | 16/38 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +4.6 | 3e-04 | 17/39 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.20× | +4.4 | 5e-04 | 11/39 (A-427, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.6 | 0.013 | 11/39 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.15× | +3.5 | 0.023 | 7/39 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.031 | 10/39 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.091 | 3/39 (HCT15, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.766×** | -6.5 | 5e-08 | 22/39 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.788×** | -5.8 | 2e-06 | 15/39 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.782×** | -5.6 | 3e-06 | 17/39 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.788×** | -5.6 | 3e-06 | 18/40 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.800×** | -5.4 | 6e-06 | 20/39 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -5.4 | 6e-06 | 1/40 (NCI-H2030) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -4.9 | 9e-05 | 13/38 (A549, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.686×** | -4.8 | 1e-04 | 14/39 (HS-578T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.824×** | -4.7 | 2e-04 | 13/39 (RKO, A-172, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.878× | -4.5 | 4e-04 | 12/39 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.845× | -4.1 | 0.002 | 17/39 (NCI-H1792, hTERT-HPNE, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.893× | -3.9 | 0.005 | 7/39 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.855× | -3.8 | 0.006 | 11/39 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.865× | -3.5 | 0.016 | 15/39 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.4 | 0.029 | 14/39 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.873× | -3.3 | 0.033 | 9/39 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.875× | -3.2 | 0.039 | 12/39 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.876× | -3.2 | 0.039 | 15/39 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 0.882× | -3.0 | 0.065 | 16/39 (NCI-H1792, hTERT-HPNE, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -12.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.323× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 168 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.323× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.4) |
| [[PANC-1 (line)]] | alt | 14.6 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.31× (z +22.0) | — |
| [[A-427 (line)]] | wt | 91.8 | 2 | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.17× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -11.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 23.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +14.7) | [[Digitoxin (drug)]] 5 µM 0.201× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 77.2 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 107 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +14.5) | — |
| [[LoVo (line)]] | wt | 40.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 264 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -11.3) ⚠ cell-cycle shift, explains ~21% of this change |
| [[Panc 03.27 (line)]] | alt | 77.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 11.7× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 53.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SW480 (line)]] | alt | 22.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +17.8) | — |
| [[A498 (line)]] | wt | 86.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +15.9) | — |
| [[HCT15 (line)]] | alt | 33.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +13.0) | — |
| [[J82 (line)]] | alt | 63.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.41× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -9.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H1573 (line)]] | alt | 28.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -9.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[RKO (line)]] | wt | 43.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[A549 (line)]] | wt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.5) | — |
| [[C32 (line)]] | wt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 41.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +10.6) | — |
| [[KATO III (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 52.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.35× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 83.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -9.3) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SW 1088 (line)]] | alt | 82.2 | 0 | 1 | — | [[Posaconazole (drug)]] 0.5 µM 0.0876× (z -8.5) |
| [[AN3 CA (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01828]] | +0.67 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[HMGN2P46]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[GATM]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[KCNIP1]] | +0.62 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PIK3IP1-DT]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[IL1A]] | +0.59 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[SLAMF7]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SYT16]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FRMD6-AS2]] | +0.59 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[MSANTD3]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[IL6]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5]] | -0.55 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[PYGB]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[NUP160]] | -0.52 | -0.52 / -0.38 | both halves | 7e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PACSIN2]] | -0.52 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR155HG]] | B | MIR155HG activity raises DSE's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without MIR155HG | 0.033 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[GPR176]] | B | GPR176 activity raises DSE's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 2.94× lower at baseline in the lines without GPR176 | 0.046 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[BNC2]] | B | BNC2 activity raises DSE's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.45× lower at baseline in the lines without BNC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[FGFR1]] | B | FGFR1 activity raises DSE's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.90× lower at baseline in the lines without FGFR1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |
| [[TOP2A]] | B | TOP2A activity lowers DSE's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[IL1B]] | B | IL1B activity raises DSE's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.40× lower at baseline in the lines without IL1B | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[KIRREL3]] | B | KIRREL3 activity raises DSE's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 2.61× lower at baseline in the lines without KIRREL3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[LINC03041]] | B | LINC03041 activity raises DSE's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 2.75× lower at baseline in the lines without LINC03041 | 0.077 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[PTGS2]] | B | PTGS2 activity weakens DSE's drug response | lines that do not express PTGS2 (20) vs lines expressing it (20) | the lines without PTGS2 respond 1.51× as strongly (z diff -1.45); strongest at Idarubicin (hydrochloride) 5 µM: 3.09x vs 1.58x (z diff -4.5) | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; target measured in part of the lines; artifact flags |
| [[ZEB2]] | B | ZEB2 activity raises DSE's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 2.79× lower at baseline in the lines without ZEB2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16 |
| [[RFTN1]] | B | RFTN1 activity raises DSE's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without RFTN1 | 0.083 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[C1QTNF1]] | B | C1QTNF1 activity raises DSE's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without C1QTNF1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT3]] | B | DSE activity raises AKT3's level | lines that do not express DSE (9) vs lines expressing it (41) | 6.36× lower at baseline in the lines without DSE | 0.062 | ⚠ within organs, on part of the lines; also absent: SGCE, WDR17, LRP12; maybe low, not absent |
| [[MIR155HG]] | B | DSE activity raises MIR155HG's level | lines that do not express DSE (9) vs lines expressing it (41) | 2.52× lower at baseline in the lines without DSE | 0.084 | ⚠ within organs, on part of the lines; also absent: SGCE, WDR17, LRP12; maybe low, not absent |
| [[FGF12]] | B | DSE activity raises FGF12's level | lines that do not express DSE (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without DSE | 0.090 | ⚠ within organs, on part of the lines; also absent: SGCE, WDR17, LRP12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.5, 0.3); signed map (40.3, 12.0). **Vector** length 118, 30.0% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.51 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.55 to 5); *KRAS signaling up* (hallmark, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +31.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +21.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.0 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -3.8 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.3 | -5.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.3 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | dermatan sulfate epimerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:116,254,173-116,444,861 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DSEPI, DS-Epi1; previously SART2 |
| Reactome | 4 pathways, smallest: DS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL01](https://www.uniprot.org/uniprotkb/Q9UL01) (Dermatan-sulfate epimerase):

> Converts D-glucuronic acid to L-iduronic acid (IdoUA) residues. Plays an important role in the biosynthesis of the glycosaminoglycan/mucopolysaccharide dermatan sulfate.

**Summary**, from NCBI Gene [29940](https://www.ncbi.nlm.nih.gov/gene/29940):

> The protein encoded by this gene is a tumor-rejection antigen. It is localized to the endoplasmic reticulum and functions to convert D-glucuronic acid to L-iduronic acid during the biosynthesis of dermatan sulfate. This antigen possesses tumor epitopes capable of inducing HLA-A24-restricted and tumor-specific cytotoxic T lymphocytes in cancer patients and may be useful for specific immunotherapy. Mutations in this gene cause inmusculocontractural Ehlers-Danlos syndrome. Alternative splicing …

**Accessions** — [HGNC:21144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21144) · Entrez [29940](https://www.ncbi.nlm.nih.gov/gene/29940) · UniProt [Q9UL01](https://www.uniprot.org/uniprotkb/Q9UL01) · Ensembl [ENSG00000111817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111817)

## Data

Gene col 3287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3287); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3287]; `tensor/DDL_lfc|DDL_z.npy` [3287]; `embed/gene_vectors.npy` [3287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3287 or target_col == 3287). Every well: [[DSE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

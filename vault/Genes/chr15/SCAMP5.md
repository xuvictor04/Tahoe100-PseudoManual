---
symbol: "SCAMP5"
type: "gene"
col: 12680
ensembl_id: "ENSG00000198794"
name: "secretory carrier membrane protein 5"
location: "15q24.2"
module: 21
arm: "+"
pooled_cpm: 8.51
n_lines_expressing: 47
n_dd_up: 30
n_dd_down: 16
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 31
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SCAMP5

*secretory carrier membrane protein 5* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.35× (z +33.9, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.442× (z -11.7, q 8e-29, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UPP2]] (+0.65, fdr 7e-06), [[SPATA1]] (+0.65, fdr 2e-05), [[CATSPER2P1-1]] (+0.64, fdr 6e-05); moves opposite to [[H2AX]] (-0.53, fdr 4e-05), [[SPTAN1]] (-0.52, fdr 1e-04), [[BCL7B]] (-0.51, fdr 5e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GLS2]] → it (grade B ⚠); 31 go from it, the strongest it → cells under [[Peretinoin (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.35×** | +33.9 | 0e+00 | 37/39 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +15.8 | 0e+00 | 26/37 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +13.5 | 4e-39 | 29/40 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +12.8 | 4e-35 | 31/44 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +9.6 | 6e-20 | 18/32 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +9.3 | 9e-19 | 26/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.49×** | +8.1 | 4e-14 | 20/44 (A498, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +7.5 | 4e-12 | 21/45 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +6.4 | 1e-08 | 21/45 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +6.2 | 3e-08 | 17/43 (KATO III, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +6.1 | 6e-08 | 19/45 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +5.5 | 1e-06 | 3/21 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.1 | 2e-05 | 10/40 (KATO III, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 2e-05 | 15/44 (A498, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 2e-04 | 17/45 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 9e-04 | 8/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.003 | 7/45 (KATO III, NCI-H2347, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 8/45 (Hs 766T, C-33 A, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.009 | 7/44 (KATO III, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -11.7 | 8e-29 | 33/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -10.4 | 4e-23 | 26/43 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.640×** | -9.0 | 3e-17 | 21/41 (A498, NCI-H23, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.565×** | -8.2 | 4e-14 | 23/38 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.629×** | -6.6 | 4e-09 | 20/42 (SNU-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.670×** | -5.7 | 9e-07 | 18/38 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -5.5 | 4e-06 | 17/35 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.717×** | -4.8 | 1e-04 | 12/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -4.6 | 3e-04 | 12/43 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -4.2 | 0.001 | 15/44 (NCI-H2030, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.737×** | -4.2 | 0.001 | 12/44 (NCI-H23, NCI-H2347, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -3.9 | 0.004 | 15/43 (KATO III, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.797×** | -3.2 | 0.047 | 9/44 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.798×** | -3.2 | 0.047 | 5/45 (NCI-H2030, A498, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.649×** | -3.2 | 0.047 | 8/37 (KATO III, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.812×** | -3.0 | 0.099 | 0/44 | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.9 | 2 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +17.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -13.3) |
| [[KATO III (line)]] | alt | 25.4 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.121× (z -13.3) |
| [[A498 (line)]] | wt | 15.8 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -12.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[LOX-IMVI (line)]] | wt | 4.27 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +12.8) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0768× (z -8.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 9.45 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +12.5) | [[Harringtonine (drug)]] 5 µM 0.0853× (z -10.6) ⚠ cell-cycle shift, explains ~89% of this change |
| [[LoVo (line)]] | wt | 9.19 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +16.7) | [[Digitoxin (drug)]] 5 µM 0.0544× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 3.67 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +8.6) | [[Daptomycin (drug)]] 0.5 µM 0.0483× (z -9.2) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 9.60 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 2.31 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0625× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.206× (z -8.5) |
| [[SW 900 (line)]] | alt | 8.56 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.106× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 5.44 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.28× (z +15.0) | — |
| [[A549 (line)]] | wt | 8.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +15.8) | — |
| [[AsPC-1 (line)]] | alt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.8× (z +14.5) | — |
| [[C-33 A (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 7.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 5.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.42× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.99× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 3.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 9.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 4.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.5× (z +14.5) | — |
| [[NCI-H2347 (line)]] | alt | 8.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +11.2) | — |
| [[RKO (line)]] | wt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -9.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 34.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +15.0) | — |
| [[SW48 (line)]] | wt | 8.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +9.1) | — |
| [[A-172 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPP2]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.65 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[CATSPER2P1-1]] | +0.64 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[SEPTIN1]] | +0.61 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[CCNO-DT]] | +0.61 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SLC12A9]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LANCL1-AS1]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[C2CD5-AS1]] | +0.59 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ADAP2]] | +0.59 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[TERB1]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.59 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[LRRC8C-DT]] | +0.58 | +0.46 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H2AX]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SPTAN1]] | -0.52 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[BCL7B]] | -0.51 | -0.24 / -0.58 | both halves | 5e-04 |  |
| [[RNF123]] | -0.51 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[WDR70]] | -0.50 | -0.19 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[MAP9]] | -0.50 | -0.23 / -0.25 | both halves | 5e-04 |  |
| [[POLR2E]] | -0.50 | -0.24 / -0.40 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLS2]] | B | GLS2 activity raises SCAMP5's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without GLS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SCAMP5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Peretinoin (drug)]] 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Peretinoin 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.49× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Daptomycin (drug)]] 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.55× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent; cell counts less trustworthy |
| cells under [[Glycyrrhizic acid (drug)]] 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.67× the cells of the other lines | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | C | SCAMP5 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.68× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Epirubicin (hydrochloride) (drug)]] 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Epirubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.75× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Mozavaptan (drug)]] 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Mozavaptan 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.67× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Pitavastatin (Calcium) (drug)]] 5 µM | C | SCAMP5 activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.70× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.73× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Panobinostat (drug)]] 5 µM | C | SCAMP5 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.58× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | C | SCAMP5 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.65× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.66× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| cells under [[γ-Oryzanol (drug)]] 0.05 µM | C | SCAMP5 activity lowers the cells' numbers under γ-Oryzanol 0.05 µM (makes them more sensitive) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 1.33× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.0, 25.6); signed map (34.3, -0.1). **Vector** length 64.0, 9.86% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +33.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.4 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -2.0 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.4 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.0 | -2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | secretory carrier membrane protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:74,957,219-75,021,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24969 |
| Gene groups (HGNC) | Secretory carrier membrane proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAC9](https://www.uniprot.org/uniprotkb/Q8TAC9) (Secretory carrier-associated membrane protein 5):

> Required for the calcium-dependent exocytosis of signal sequence-containing cytokines such as CCL5. Probably acts in cooperation with the SNARE machinery. May play a role in accumulation of expanded polyglutamine (polyQ) protein huntingtin (HTT) in case of endoplasmic reticulum stress by inhibiting the endocytosis pathway.

**Summary**, from NCBI Gene [192683](https://www.ncbi.nlm.nih.gov/gene/192683):

> Involved in positive regulation of cytokine production; regulation of vesicle-mediated transport; and response to endoplasmic reticulum stress. Located in Golgi apparatus; plasma membrane; and recycling endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30386) · Entrez [192683](https://www.ncbi.nlm.nih.gov/gene/192683) · UniProt [Q8TAC9](https://www.uniprot.org/uniprotkb/Q8TAC9) · Ensembl [ENSG00000198794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198794)

## Data

Gene col 12680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12680); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12680]; `tensor/DDL_lfc|DDL_z.npy` [12680]; `embed/gene_vectors.npy` [12680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12680 or target_col == 12680). Every well: [[SCAMP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAMP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

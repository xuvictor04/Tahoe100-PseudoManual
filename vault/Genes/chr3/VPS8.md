---
symbol: "VPS8"
type: "gene"
col: 8025
ensembl_id: "ENSG00000156931"
name: "VPS8 subunit of CORVET complex"
location: "3q27.2"
module: 230
arm: "+"
pooled_cpm: 116.83
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/230"]
generated_by: "tahoemap"
---

# VPS8

*VPS8 subunit of CORVET complex* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.76× (z +18.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.522× (z -11.9, q 5e-30, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.657× (z -10.9, q 2e-25, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS41]] (+0.64, fdr 7e-06), [[GTF2H2]] (+0.58, fdr 1e-05), [[UBXN2B]] (+0.55, fdr 1e-04); moves opposite to [[PIPOX]] (-0.60, fdr 9e-05), [[NIPBL-DT]] (-0.59, fdr 6e-05), [[STARD4-AS1]] (-0.55, fdr 0.001, ⚠ one half only (not replicated)), [[RALY-AS1]] (-0.54, fdr 2e-04).
> It is in [[Module 230]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.76×** | +18.6 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.69×** | +18.1 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +14.6 | 1e-45 | 46/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +7.3 | 5e-11 | 32/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.2 | 6e-11 | 36/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.1 | 3e-05 | 30/48 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +4.6 | 3e-04 | 41/49 (SW480, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 0.001 | 27/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.006 | 27/48 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 1.16× | +3.9 | 0.006 | 14/48 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.016 | 26/48 (J82, H4, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.5 | 0.021 | 20/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.037 | 8/48 (J82, A-172, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.14× | +3.3 | 0.037 | 7/48 (J82, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -11.9 | 5e-30 | 41/49 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.509×** | -11.5 | 5e-28 | 40/45 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -10.9 | 2e-25 | 36/49 (LOX-IMVI, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -9.6 | 1e-19 | 34/44 (HEC-1-A, SW48, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.759×** | -5.1 | 4e-05 | 31/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -4.9 | 7e-05 | 31/49 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.798×** | -4.0 | 0.005 | 27/47 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.014 | 21/48 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.6 | 0.017 | 25/48 (SK-MEL-2, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 117 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -11.4) |
| [[HOP62 (line)]] | alt | 107 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.01× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 147 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 192 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 124 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.84× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.316× (z -13.1) |
| [[SW480 (line)]] | alt | 186 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -16.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 89.3 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.6) |
| [[KATO III (line)]] | alt | 177 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -12.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 118 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.409× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 125 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -26.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 88.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +23.9) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 178 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -8.6) |
| [[SW1417 (line)]] | alt | 123 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -12.8) ⚠ toxic |
| [[H4 (line)]] | wt | 114 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 85.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -21.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 77.4 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.29× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 118 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.8) |
| [[SW48 (line)]] | wt | 139 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.62× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -11.3) |
| [[A549 (line)]] | wt | 94.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 86.3 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.8) |
| [[COLO 205 (line)]] | alt | 116 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 84.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.72× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 91.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -13.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 95.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -11.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 113 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.50× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.54× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 35.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 114 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +13.5) | — |
| [[C32 (line)]] | wt | 133 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -17.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 112 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.00× (z +15.3) | — |
| [[J82 (line)]] | alt | 106 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.1) | [[Ixazomib citrate (drug)]] 5 µM 0.395× (z -10.1) |
| [[LS 180 (line)]] | wt | 100 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.68× (z +14.2) | — |
| [[RKO (line)]] | wt | 117 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 110 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.5) |
| [[SW 900 (line)]] | alt | 49.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.25× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 98.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -9.5) |
| [[HCT15 (line)]] | alt | 131 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 124 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -10.1) |
| [[A-427 (line)]] | wt | 241 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -13.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[C-33 A (line)]] | alt | 109 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 88.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.47× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 91.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0836× (z -8.8) |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS41]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 | same gene group; STRING 898 |
| [[GTF2H2]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 | same gene group |
| [[UBXN2B]] | +0.55 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[STX8]] | +0.55 | +0.27 / +0.53 | both halves | 3e-04 | STRING 553 |
| [[MOSPD2]] | +0.55 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[METTL5]] | +0.54 | +0.25 / +0.61 | both halves | 4e-04 |  |
| [[FRA10AC1]] | +0.54 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[DTNBP1]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[WASHC4]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PRXL2C]] | +0.53 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[AVL9]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[FKBP15]] | +0.51 | +0.37 / +0.53 | both halves | 9e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIPOX]] | -0.60 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[NIPBL-DT]] | -0.59 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[STARD4-AS1]] | -0.55 | -0.17 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[RALY-AS1]] | -0.54 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[C9]] | -0.54 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[GSK3B-DT]] | -0.52 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[THUMPD3-AS1]] | -0.52 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[LINC00863]] | -0.52 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[TGFB3]] | -0.51 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[KLHL3]] | -0.51 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PANK2]] | -0.51 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[POC1B-AS1]] | -0.51 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[FBXL8]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 230]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.3, 14.8); signed map (-20.0, -11.9). **Vector** length 104, 34.6% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +18.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +18.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -15.3 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | VPS8 subunit of CORVET complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:184,812,143-185,052,614 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32099; previously KIAA0804 |
| Gene groups (HGNC) | Ring finger proteins; CORVET complex; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3P4](https://www.uniprot.org/uniprotkb/Q8N3P4) (Vacuolar protein sorting-associated protein 8 homolog):

> Plays a role in vesicle-mediated protein trafficking of the endocytic membrane transport pathway. Believed to act as a component of the putative CORVET endosomal tethering complexes which is proposed to be involved in the Rab5-to-Rab7 endosome conversion probably implicating MON1A/B, and via binding SNAREs and SNARE complexes to mediate tethering and docking events during SNARE-mediated membrane fusion. The CORVET complex is proposed to function as a Rab5 effector to mediate early endosome …

**Summary**, from NCBI Gene [23355](https://www.ncbi.nlm.nih.gov/gene/23355):

> Predicted to enable protein-membrane adaptor activity. Involved in endosomal vesicle fusion. Located in early endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29122) · Entrez [23355](https://www.ncbi.nlm.nih.gov/gene/23355) · UniProt [Q8N3P4](https://www.uniprot.org/uniprotkb/Q8N3P4) · Ensembl [ENSG00000156931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156931)

## Data

Gene col 8025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8025); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8025]; `tensor/DDL_lfc|DDL_z.npy` [8025]; `embed/gene_vectors.npy` [8025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8025 or target_col == 8025). Every well: [[VPS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

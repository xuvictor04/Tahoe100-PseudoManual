---
symbol: "TUFT1"
type: "gene"
col: 6723
ensembl_id: "ENSG00000143367"
name: "tuftelin 1"
location: "1q21.3"
module: 44
arm: "+"
pooled_cpm: 99.34
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 31
direction_downstream: 1
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# TUFT1

*tuftelin 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 5.14× (z +18.5, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.529× (z -10.2, q 9e-22, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIMA1]] (+0.69, fdr 7e-06), [[CTNND1]] (+0.67, fdr 7e-06), [[LMCD1]] (+0.66, fdr 7e-06); moves opposite to [[TMEM11-DT]] (-0.58, fdr 1e-05), [[MOSMO]] (-0.57, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.57, fdr 1e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[USP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.14×** | +18.5 | 0e+00 | 44/44 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +18.4 | 0e+00 | 42/44 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.79×** | +15.1 | 0e+00 | 44/44 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.55×** | +14.4 | 1e-44 | 44/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +9.2 | 5e-18 | 41/44 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.19×** | +8.5 | 1e-15 | 35/44 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +8.3 | 7e-15 | 33/44 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.95×** | +7.6 | 3e-12 | 35/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +6.4 | 1e-08 | 31/44 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.52×** | +5.3 | 7e-06 | 33/46 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 4e-05 | 34/45 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +4.9 | 6e-05 | 30/45 (RKO, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.8 | 6e-05 | 23/44 (KATO III, HCT15, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 2e-04 | 25/45 (A-172, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.49×** | +4.5 | 3e-04 | 27/45 (SHP-77, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -10.2 | 9e-22 | 36/45 (NCI-H2347, HT-29, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -9.0 | 4e-17 | 30/35 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.568×** | -6.4 | 3e-08 | 31/45 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.741×** | -4.8 | 2e-04 | 26/44 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.676×** | -4.1 | 0.004 | 25/39 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -3.4 | 0.075 | 24/46 (NCI-H2347, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.075 | 23/44 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.082 | 24/44 (NCI-H1573, SHP-77, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.0 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +20.3) | — |
| [[A-172 (line)]] | wt | 117 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +17.6) | — |
| [[A-427 (line)]] | wt | 30.5 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +16.3) | — |
| [[Panc 03.27 (line)]] | alt | 167 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 235 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -14.2) |
| [[KATO III (line)]] | alt | 82.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +15.6) | — |
| [[SW1417 (line)]] | alt | 209 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -10.9) |
| [[A549 (line)]] | wt | 83.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.97× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 187 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 89.0 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.7) |
| [[Hs 766T (line)]] | wt | 56.6 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 7.63× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -9.4) |
| [[HS-578T (line)]] | alt | 37.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 289 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 11.3× (z +15.7) | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +23.7) | — |
| [[NCI-H23 (line)]] | alt | 30.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +17.1) | — |
| [[NCI-H2347 (line)]] | alt | 217 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -19.5) |
| [[SNU-423 (line)]] | alt | 79.5 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 6.44× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -8.9) |
| [[A498 (line)]] | wt | 153 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +15.6) | — |
| [[J82 (line)]] | alt | 130 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 78.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.42× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 51.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.67× (z +13.2) | — |
| [[RKO (line)]] | wt | 65.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 53.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +17.2) | — |
| [[SW480 (line)]] | alt | 74.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.6) | — |
| [[COLO 205 (line)]] | alt | 272 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -13.6) |
| [[LoVo (line)]] | wt | 114 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +9.5) | — |
| [[NCI-H661 (line)]] | alt | 65.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -9.6) |
| [[SW 900 (line)]] | alt | 139 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -10.4) |
| [[HCT15 (line)]] | alt | 70.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.06× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 147 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 168 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.6) |
| [[AN3 CA (line)]] | alt | 53.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -8.5) |
| [[C-33 A (line)]] | alt | 28.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.50× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 91.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -8.8) |
| [[SHP-77 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 54.2 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0685× (z -8.7) |
| [[SW48 (line)]] | wt | 45.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.11× (z +9.5) | — |
| [[C32 (line)]] | wt | 9.76 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMA1]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 | same gene group |
| [[CTNND1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[LMCD1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[USP2]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CGN]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 | ⚠ same locus (1.6 kb, same strand: neighbours can correlate without regulation) |
| [[RHPN2]] | +0.60 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[TPPP]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[MAPRE2]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[STARD5]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[BIK]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[KLF2]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[RAB30]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[MOSMO]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[E2F3]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[NAF1]] | -0.56 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ANAPC1]] | -0.55 | -0.53 / -0.41 | both halves | 4e-05 | same gene group |
| [[DUS2]] | -0.55 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MSANTD2]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DNAAF10]] | -0.54 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[TLCD3A]] | -0.53 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[NHSL1]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 | same gene group |
| [[PRDM15]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 30, C 1. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity raises TUFT1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.88× lower at baseline in the lines without ELF3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[CDH1]] | B | CDH1 activity raises TUFT1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[IRF6]] | B | IRF6 activity raises TUFT1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.53× lower at baseline in the lines without IRF6 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[JUP]] | B | JUP activity raises TUFT1's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.84× lower at baseline in the lines without JUP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TUFT1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.04× lower at baseline in the lines without ELF3-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[ST14]] | B | ST14 activity raises TUFT1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.64× lower at baseline in the lines without ST14 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[TSPAN15]] | B | TSPAN15 activity raises TUFT1's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without TSPAN15 | 0.004 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises TUFT1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.89× lower at baseline in the lines without ATP8B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TJP3]] | B | TJP3 activity raises TUFT1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TJP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[CGN]] | B | CGN activity raises TUFT1's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without CGN | 0.016 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[RHOV]] | B | RHOV activity raises TUFT1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without RHOV | 0.024 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[HHLA2]] | B | HHLA2 activity raises TUFT1's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without HHLA2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP2]] | C | TUFT1 activity raises USP2's level | lines that do not express TUFT1 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without TUFT1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with TERT; also absent: FZD5, GRHL1, DBNDD2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.363). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.1, 1.2); signed map (-0.7, 20.9). **Vector** length 131, 45.6% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +9.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.3 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.3 | +3.2 |
|  | [[Trametinib (drug)]] 5 µM |  | +5.1 | +5.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.0 | +4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.1 | +3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.6 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.9 | -4.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.6 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.3 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | tuftelin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,540,305-151,583,583 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NNX1](https://www.uniprot.org/uniprotkb/Q9NNX1) (Tuftelin):

> Involved in the structural organization of the epidermis. Involved in the mineralization and structural organization of enamel.

**Summary**, from NCBI Gene [7286](https://www.ncbi.nlm.nih.gov/gene/7286):

> Tuftelin is an acidic protein that is thought to play a role in dental enamel mineralization and is implicated in caries susceptibility. It is also thought to be involved with adaptation to hypoxia, mesenchymal stem cell function, and neurotrophin nerve growth factor mediated neuronal differentiation. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:12422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12422) · Entrez [7286](https://www.ncbi.nlm.nih.gov/gene/7286) · UniProt [Q9NNX1](https://www.uniprot.org/uniprotkb/Q9NNX1) · Ensembl [ENSG00000143367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143367)

## Data

Gene col 6723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6723); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6723]; `tensor/DDL_lfc|DDL_z.npy` [6723]; `embed/gene_vectors.npy` [6723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6723 or target_col == 6723). Every well: [[TUFT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUFT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

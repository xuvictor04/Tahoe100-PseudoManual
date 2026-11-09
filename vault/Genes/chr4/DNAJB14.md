---
symbol: "DNAJB14"
type: "gene"
col: 8837
ensembl_id: "ENSG00000164031"
name: "DnaJ heat shock protein family (Hsp40) member B14"
location: "4q23"
module: 83
arm: "+"
pooled_cpm: 104.83
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# DNAJB14

*DnaJ heat shock protein family (Hsp40) member B14* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.32× (z +9.1, q 3e-17, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.369× (z -23.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP5M1]] (+0.74, fdr 1e-05), [[CUL1]] (+0.65, fdr 5e-05), [[GGPS1]] (+0.64, fdr 3e-05); moves opposite to [[ARRB2]] (-0.72, fdr 1e-05), [[STARD5]] (-0.63, fdr 1e-04), [[KCTD17]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +9.1 | 3e-17 | 29/48 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.9 | 9e-07 | 22/49 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.8 | 3e-04 | 24/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.8 | 3e-04 | 23/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +3.6 | 0.032 | 18/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.032 | 14/48 (SW 900, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.369×** | -23.4 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.379×** | -22.7 | 0e+00 | 48/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.505×** | -16.0 | 0e+00 | 44/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.742×** | -7.0 | 4e-10 | 33/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.773×** | -5.8 | 8e-07 | 23/44 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.789×** | -5.3 | 1e-05 | 25/47 (RKO, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.803×** | -5.1 | 2e-05 | 24/49 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -5.1 | 2e-05 | 20/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.814×** | -4.6 | 2e-04 | 24/47 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.6 | 0.021 | 0/50 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.043 | 18/48 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | 0.860× | -3.3 | 0.053 | 20/45 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.911× | -3.1 | 0.093 | 3/48 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.875× | -3.0 | 0.10 | 10/48 (hTERT-HPNE, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 131 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -19.7) |
| [[SW480 (line)]] | alt | 84.6 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -24.5) |
| [[KATO III (line)]] | alt | 96.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -19.8) |
| [[LOX-IMVI (line)]] | wt | 98.6 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +19.4) | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -15.6) |
| [[RKO (line)]] | wt | 145 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 110 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.400× (z -11.8) |
| [[SW 900 (line)]] | alt | 110 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -11.9) |
| [[A498 (line)]] | wt | 131 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +22.3) | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -14.8) |
| [[COLO 205 (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 91.4 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -10.6) |
| [[HOP62 (line)]] | alt | 120 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -20.6) |
| [[HS-578T (line)]] | alt | 80.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.209× (z -17.0) |
| [[HT-29 (line)]] | alt | 129 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -18.7) |
| [[hTERT-HPNE (line)]] | wt | 141 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -10.2) |
| [[J82 (line)]] | alt | 77.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -10.4) |
| [[LoVo (line)]] | wt | 98.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +22.4) | [[Panobinostat (drug)]] 5 µM 0.276× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 102 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.447× (z -11.8) |
| [[PANC-1 (line)]] | alt | 122 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -17.6) |
| [[SNU-423 (line)]] | alt | 55.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.296× (z -12.3) |
| [[A-172 (line)]] | wt | 115 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -17.4) |
| [[A549 (line)]] | wt | 76.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -14.3) |
| [[CHP-212 (line)]] | wt | 107 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -9.8) |
| [[H4 (line)]] | wt | 144 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 89.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -13.1) |
| [[Hs 766T (line)]] | wt | 101 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.518× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 105 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +31.1) | [[Panobinostat (drug)]] 5 µM 0.373× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -15.2) |
| [[SHP-77 (line)]] | alt | 74.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -11.9) |
| [[SW1417 (line)]] | alt | 80.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -12.4) |
| [[A-427 (line)]] | wt | 132 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.398× (z -11.9) |
| [[C-33 A (line)]] | alt | 139 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -12.4) |
| [[C32 (line)]] | wt | 111 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +32.2) | — |
| [[HCT15 (line)]] | alt | 167 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 98.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 82.6 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.481× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 110 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -8.7) |
| [[SW48 (line)]] | wt | 130 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 96.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 88.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 118 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP5M1]] | +0.74 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[CUL1]] | +0.65 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[GGPS1]] | +0.64 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[C11orf58]] | +0.64 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[TIRAP]] | +0.63 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[IGF2BP1]] | +0.62 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[DPP8]] | +0.62 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[FBXO30]] | +0.62 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CENPL]] | +0.62 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[ZNF407-AS1]] | +0.62 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[PRR3]] | +0.61 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[GABPB1]] | +0.61 | +0.48 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRB2]] | -0.72 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[STARD5]] | -0.63 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[KCTD17]] | -0.61 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[USP2]] | -0.60 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[MLF1]] | -0.60 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TCIRG1]] | -0.59 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[SMARCD3]] | -0.59 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[RHPN1]] | -0.58 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.58 | -0.46 / -0.22 | both halves | 6e-04 |  |
| [[IMPDH2]] | -0.57 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[GTPBP3]] | -0.57 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[BAIAP3]] | -0.57 | -0.38 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DNAJB14's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.3, -5.4); signed map (19.6, -22.6). **Vector** length 118, 33.2% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.9 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -23.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -22.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -3.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.6 | -2.4 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:99,896,248-99,946,618 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14281 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBM8](https://www.uniprot.org/uniprotkb/Q8TBM8) (DnaJ homolog subfamily B member 14):

> Acts as a co-chaperone with HSPA8/Hsc70; required to promote protein folding and trafficking, prevent aggregation of client proteins, and promote unfolded proteins to endoplasmic reticulum-associated degradation (ERAD) pathway. Acts by determining HSPA8/Hsc70's ATPase and polypeptide-binding activities. Can also act independently of HSPA8/Hsc70: together with DNAJB12, acts as a chaperone that promotes maturation of potassium channels KCND2 and KCNH2 by stabilizing nascent channel subunits and …

**Summary**, from NCBI Gene [79982](https://www.ncbi.nlm.nih.gov/gene/79982):

> Enables Hsp70 protein binding activity. Involved in protein folding and protein-containing complex assembly. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25881) · Entrez [79982](https://www.ncbi.nlm.nih.gov/gene/79982) · UniProt [Q8TBM8](https://www.uniprot.org/uniprotkb/Q8TBM8) · Ensembl [ENSG00000164031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164031)

## Data

Gene col 8837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8837); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8837]; `tensor/DDL_lfc|DDL_z.npy` [8837]; `embed/gene_vectors.npy` [8837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8837 or target_col == 8837). Every well: [[DNAJB14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

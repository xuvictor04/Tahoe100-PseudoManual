---
symbol: "PFKP"
type: "gene"
col: 846
ensembl_id: "ENSG00000067057"
name: "phosphofructokinase, platelet"
location: "10p15.2"
module: 54
arm: "-"
pooled_cpm: 194.08
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# PFKP

*phosphofructokinase, platelet* — 10p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +6.8, q 8e-09, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.411× (z -15.9, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.480× (z -13.6, q 8e-40, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPAT5]] (+0.61, fdr 1e-05), [[ENO1]] (+0.53, fdr 3e-05), [[SLC6A6]] (+0.52, fdr 1e-05); moves opposite to [[BTBD7]] (-0.54, fdr 1e-04), [[CCDC66]] (-0.51, fdr 1e-04), [[WDR83OS]] (-0.51, fdr 1e-04, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[MFSD5]] (-0.50, fdr 6e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EHD2]] → it (grade B ⚠); 8 go from it, the strongest it → [[ASPH]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.8 | 8e-09 | 31/45 (RKO, KATO III, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.7 | 6e-04 | 22/45 (SW480, LoVo, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.011 | 25/45 (NCI-H460, HOP62, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.068 | 27/45 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.4 | 0.070 | 20/41 (C-33 A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +3.3 | 0.078 | 20/45 (HT-29, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.2 | 0.11 | 17/46 (C-33 A, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.2 | 0.11 | 19/45 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.12 | 15/44 (SNU-423, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.411×** | -15.9 | 0e+00 | 44/44 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -13.6 | 8e-40 | 43/45 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.602×** | -13.3 | 3e-38 | 34/45 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.493×** | -13.1 | 3e-37 | 42/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -12.2 | 6e-32 | 42/45 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.586×** | -9.5 | 1e-19 | 34/45 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.637×** | -8.4 | 4e-15 | 41/45 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.770×** | -6.8 | 6e-10 | 29/46 (A549, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -6.4 | 9e-09 | 28/45 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.710×** | -6.1 | 6e-08 | 36/45 (SK-MEL-2, HT-29, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.738×** | -5.6 | 9e-07 | 29/45 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.740×** | -5.4 | 4e-06 | 29/44 (C-33 A, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -4.9 | 4e-05 | 25/46 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.5 | 3e-04 | 24/45 (SK-MEL-2, RKO, …) | top dose only | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 0.850× | -4.3 | 8e-04 | 16/45 (A549, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.724×** | -3.1 | 0.047 | 20/46 (NCI-H23, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.846× | -3.1 | 0.053 | 18/45 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.066 | 16/44 (hTERT-HPNE, J82, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 287 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -27.6) |
| [[PANC-1 (line)]] | alt | 177 | 2 (2 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.88× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -23.1) |
| [[LOX-IMVI (line)]] | wt | 210 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -22.2) |
| [[SK-MEL-2 (line)]] | alt | 198 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -20.8) |
| [[A549 (line)]] | wt | 334 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -13.5) |
| [[HT-29 (line)]] | alt | 199 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 228 | 1 | 6 | [[Auranofin (drug)]] 5 µM 2.10× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -21.2) |
| [[SNU-423 (line)]] | alt | 286 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.417× (z -10.0) |
| [[J82 (line)]] | alt | 252 | 0 | 6 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.332× (z -14.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.409× (z -11.9) |
| [[SW48 (line)]] | wt | 318 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +18.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.354× (z -10.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 312 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.359× (z -13.6) |
| [[HS-578T (line)]] | alt | 223 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.421× (z -9.9) |
| [[KATO III (line)]] | alt | 197 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.66× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.549× (z -10.3) |
| [[RKO (line)]] | wt | 147 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.353× (z -11.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.432× (z -9.6) |
| [[SW480 (line)]] | alt | 112 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.72× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -14.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.476× (z -10.0) |
| [[BT-474 (line)]] | alt | 173 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -12.8) |
| [[C-33 A (line)]] | alt | 50.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.19× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.6) |
| [[C32 (line)]] | wt | 95.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.305× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 375 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -12.4) |
| [[Hs 766T (line)]] | wt | 196 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.328× (z -13.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.394× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 337 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 282 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -10.1) |
| [[HCT15 (line)]] | alt | 302 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -25.4) |
| [[HOP62 (line)]] | alt | 259 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.321× (z -12.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.443× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 179 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 161 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -13.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -11.7) |
| [[SHP-77 (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -9.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.382× (z -8.9) |
| [[SW 900 (line)]] | alt | 164 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.338× (z -12.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.470× (z -8.8) |
| [[A-427 (line)]] | wt | 101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -19.0) |
| [[LoVo (line)]] | wt | 127 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.511× (z -8.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 104 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 141 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 80.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.271× (z -9.9) |
| [[A498 (line)]] | wt | 206 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 169 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.0) |
| [[COLO 205 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -17.6) ⚠ toxic |
| [[H4 (line)]] | wt | 218 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -11.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 368 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.478× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -13.0) |
| [[AN3 CA (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPAT5]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ENO1]] | +0.53 | +0.46 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 892 |
| [[SLC6A6]] | +0.52 | +0.53 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[TBC1D9B]] | +0.51 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[MIR30DHG]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[HAPSTR1]] | +0.49 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[DYNC1H1]] | +0.49 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[PITRM1]] | +0.48 | +0.35 / +0.57 | both halves | 1e-04 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ANXA5]] | +0.48 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[ARFGEF3]] | +0.48 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PGK1]] | +0.48 | +0.49 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 841 |
| [[CRYBG3]] | +0.47 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[AK2]] | +0.47 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD7]] | -0.54 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[CCDC66]] | -0.51 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[WDR83OS]] ⚠ | -0.51 | -0.33 / -0.54 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MFSD5]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[USP42]] | -0.49 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[BMS1P1]] | -0.47 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[AMBRA1]] | -0.46 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[BTBD6]] | -0.45 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[MRPS24]] | -0.45 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[STX18]] | -0.45 | -0.18 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[MED4]] | -0.44 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[IQCK]] | -0.44 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[DSTYK]] | -0.44 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[CWC15]] | -0.44 | -0.27 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHD2]] | B | EHD2 activity raises PFKP's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without EHD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[ARFGEF3]] | B | ARFGEF3 activity raises PFKP's level | lines that do not express ARFGEF3 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without ARFGEF3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ARHGEF37, RHBDF2, DBNDD1; maybe low, not absent |
| [[GALNT18]] | B | GALNT18 activity raises PFKP's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without GALNT18 | 0.093 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[ERRFI1]] | C | ERRFI1 activity raises PFKP's level | lines that do not express ERRFI1 (4) vs lines expressing it (46) | 3.18× lower at baseline in the lines without ERRFI1 | 0.010 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |
| [[SLC6A6]] | C | SLC6A6 activity raises PFKP's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without SLC6A6 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASPH]] | C | PFKP activity raises ASPH's level | lines that do not express PFKP (3) vs lines expressing it (47) | 4.03× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ERRFI1]] | C | PFKP activity raises ERRFI1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 3.32× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |
| [[ARFGEF3]] | C | PFKP activity raises ARFGEF3's level | lines that do not express PFKP (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |
| [[CRYBG3]] | C | PFKP activity raises CRYBG3's level | lines that do not express PFKP (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |
| [[FAM13A-AS1]] | C | PFKP activity raises FAM13A-AS1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |
| [[ENO1]] | C | PFKP activity raises ENO1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.58× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |
| [[AMBRA1]] | C | PFKP activity lowers AMBRA1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.37× higher at baseline in the lines without PFKP | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |
| [[VPS54]] | C | PFKP activity lowers VPS54's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.47× higher at baseline in the lines without PFKP | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-23.4, 18.9); signed map (-37.5, 30.1). **Vector** length 123, 40.9% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.0 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.8 | +2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -15.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.4 | -8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -3.1 | -5.4 |
|  | [[Sodium Salicylate (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Resveratrol (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.6 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphofructokinase, platelet |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.2 — chr10:3,066,333-3,137,718 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFK-C, PFKF |
| Gene groups (HGNC) | Phosphofructokinase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, INTERFERON_GAMMA_RESPONSE, GLYCOLYSIS, HYPOXIA |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01813](https://www.uniprot.org/uniprotkb/Q01813) (ATP-dependent 6-phosphofructokinase, platelet type):

> Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis.

**Summary**, from NCBI Gene [5214](https://www.ncbi.nlm.nih.gov/gene/5214):

> This gene encodes a member of the phosphofructokinase A protein family. The encoded enzyme is the platelet-specific isoform of phosphofructokinase and plays a key role in glycolysis regulation. This gene may play a role in metabolic reprogramming in some cancers, including clear cell renal cell carcinomas, and cancer of the bladder, breast, and lung. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:8878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8878) · Entrez [5214](https://www.ncbi.nlm.nih.gov/gene/5214) · UniProt [Q01813](https://www.uniprot.org/uniprotkb/Q01813) · Ensembl [ENSG00000067057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067057)

## Data

Gene col 846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 846); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 846]; `tensor/DDL_lfc|DDL_z.npy` [846]; `embed/gene_vectors.npy` [846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 846 or target_col == 846). Every well: [[PFKP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFKP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

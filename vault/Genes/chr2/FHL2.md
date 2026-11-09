---
symbol: "FHL2"
type: "gene"
col: 3703
ensembl_id: "ENSG00000115641"
name: "four and a half LIM domains 2"
location: "2q12.2"
module: 224
arm: "+"
pooled_cpm: 165.2
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 41
n_dd_up_clean: 3
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 7
direction_downstream: 13
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# FHL2

*four and a half LIM domains 2* — 2q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 1.15× (z +3.8, q 0.069, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.300× (z -31.2, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXT1]] (+0.64, fdr 1e-05), [[TNFRSF21]] (+0.63, fdr 1e-05), [[SH3RF1]] (+0.60, fdr 7e-06); moves opposite to [[DRAM2]] (-0.50, fdr 5e-05), [[RCOR3]] (-0.48, fdr 4e-05), [[USP33]] (-0.47, fdr 3e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01348]] → it (grade B ⚠); 13 go from it, the strongest it → [[CCN2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.069 | 14/44 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.069 | 11/45 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.069 | 11/44 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.069 | 20/44 (COLO 205, SW 900, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 0.05 µM |  | 1.21× | +3.3 | 0.12 | 14/44 (H4, NCI-H2347, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | 1.19× | +3.2 | 0.14 | 14/44 (A498, NCI-H1573, …) | top dose only |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.16 | 2/44 (HEC-1-A, SW 900) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.300×** | -31.2 | 0e+00 | 42/45 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.423×** | -22.3 | 0e+00 | 39/44 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.355×** | -19.0 | 0e+00 | 42/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.363×** | -18.6 | 0e+00 | 42/44 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.396×** | -16.4 | 0e+00 | 41/44 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.423×** | -15.8 | 0e+00 | 42/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.468×** | -13.4 | 6e-39 | 41/46 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -10.8 | 4e-25 | 32/44 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -9.3 | 1e-18 | 31/43 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -9.0 | 1e-17 | 31/44 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.615×** | -8.6 | 5e-16 | 28/39 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.651×** | -7.6 | 2e-12 | 28/44 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -7.5 | 4e-12 | 30/44 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.668×** | -7.4 | 5e-12 | 32/44 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.756×** | -7.2 | 2e-11 | 27/44 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -6.8 | 3e-10 | 34/44 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.699×** | -6.6 | 2e-09 | 30/44 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.703×** | -6.5 | 3e-09 | 26/44 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 350 | 0 | 19 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -26.5) |
| [[NCI-H1573 (line)]] | alt | 178 | 0 | 17 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -13.8) |
| [[LoVo (line)]] | wt | 285 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0856× (z -24.3) |
| [[J82 (line)]] | alt | 159 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -19.6) |
| [[RKO (line)]] | wt | 416 | 0 | 13 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -22.9) |
| [[COLO 205 (line)]] | alt | 308 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -21.9) |
| [[PANC-1 (line)]] | alt | 388 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0998× (z -28.9) |
| [[SHP-77 (line)]] | alt | 123 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -17.6) |
| [[SW 900 (line)]] | alt | 242 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -21.5) |
| [[NCI-H2347 (line)]] | alt | 126 | 0 | 10 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -18.6) |
| [[HepG2_C3A (line)]] | wt | 205 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -23.8) |
| [[LS 180 (line)]] | wt | 393 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -23.4) |
| [[SW48 (line)]] | wt | 482 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -19.5) |
| [[HOP62 (line)]] | alt | 149 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -20.7) |
| [[NCI-H1792 (line)]] | alt | 197 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 226 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -19.2) |
| [[KATO III (line)]] | alt | 140 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -18.9) |
| [[NCI-H23 (line)]] | alt | 188 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -24.6) |
| [[SW1417 (line)]] | alt | 243 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -24.4) |
| [[SW480 (line)]] | alt | 76.5 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -19.7) |
| [[H4 (line)]] | wt | 149 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 81.9 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.9) |
| [[A498 (line)]] | wt | 169 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 310 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -30.0) |
| [[BT-474 (line)]] | alt | 56.5 | 0 | 4 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -10.0) |
| [[C32 (line)]] | wt | 133 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -14.3) |
| [[CHP-212 (line)]] | wt | 141 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 70.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.0) |
| [[A-172 (line)]] | wt | 68.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.2) |
| [[C-33 A (line)]] | alt | 57.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -9.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 78.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -16.1) |
| [[SNU-1 (line)]] | wt | 60.2 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.255× (z -9.2) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -15.9) |
| [[A549 (line)]] | wt | 73.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 45.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.3) |
| [[Hs 766T (line)]] | wt | 83.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.8) |
| [[HS-578T (line)]] | alt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -13.6) |
| [[A-427 (line)]] | wt | 27.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXT1]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF21]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 | pathway: PPARA activates gene expression |
| [[SH3RF1]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MIR222HG]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NCEH1]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[F2RL1]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[STK17A]] | +0.53 | +0.55 / +0.46 | both halves | 3e-05 | STRING 428 |
| [[C3orf52]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CCN1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[TRIB1]] | +0.52 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[VPS37B]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[KITLG]] | +0.52 | +0.37 / +0.52 | both halves | 9e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM2]] | -0.50 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[RCOR3]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[USP33]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[FHIP2A]] | -0.46 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[CHPT1]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[KATNAL1]] | -0.45 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[PEX11A]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[FCHO2]] | -0.44 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[MLLT10]] | -0.44 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[LINC02269]] | -0.44 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[SOS1]] | -0.42 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[ABCB10]] | -0.42 | -0.32 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01348]] | B | LINC01348 activity raises FHL2's level | lines that do not express LINC01348 (10) vs lines expressing it (40) | 2.10× lower at baseline in the lines without LINC01348 | 0.025 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[CREB5]] | B | CREB5 activity raises FHL2's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without CREB5 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[TRIB1]] | B | TRIB1 activity raises FHL2's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 3.34× lower at baseline in the lines without TRIB1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[SMIM31]] | B | SMIM31 activity strengthens FHL2's drug response | lines that do not express SMIM31 (30) vs lines expressing it (16) | the lines without SMIM31 respond 0.87× as strongly (z diff +1.64); strongest at Belinostat 5 µM: 0.45x vs 0.29x (z diff +2.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; target measured in part of the lines; artifact flags |
| [[SMIM31]] | B | SMIM31 activity raises FHL2's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without SMIM31 | 0.084 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[DELEC1]] | B | DELEC1 activity raises FHL2's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without DELEC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[SYNJ2]] | C | SYNJ2 activity raises FHL2's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.68× lower at baseline in the lines without SYNJ2 | 0.056 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN2]] | C | FHL2 activity lowers CCN2's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 6.15× higher at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[TRIB1]] | C | FHL2 activity raises TRIB1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 3.35× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[SHB]] | C | FHL2 activity raises SHB's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[C3orf52]] | C | FHL2 activity raises C3orf52's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 2.95× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[SH3RF1]] | C | FHL2 activity raises SH3RF1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[CSRNP1]] | C | FHL2 activity raises CSRNP1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[PRDX6-AS1]] | C | FHL2 activity lowers PRDX6-AS1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 1.88× higher at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[ABCB10]] | C | FHL2 activity lowers ABCB10's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |
| [[HRH1]] | C | FHL2 activity raises HRH1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 3.81× lower at baseline in the lines without FHL2 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent |
| [[LINC01348]] | C | FHL2 activity raises LINC01348's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without FHL2 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent |
| [[SYNJ2]] | C | FHL2 activity raises SYNJ2's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 3.20× lower at baseline in the lines without FHL2 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent |
| [[TNFRSF21]] | C | FHL2 activity raises TNFRSF21's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 3.46× lower at baseline in the lines without FHL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.4, 14.3); signed map (15.7, 42.0). **Vector** length 111, 36.9% of its response variance represented; |z| ≥ 3 in 1,724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.1 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | -22.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +4.0 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.2 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +1.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -2.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.2 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | four and a half LIM domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.2 — chr2:105,357,712-105,438,513 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FHL-2, SLIM3, DRAL |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | UV_RESPONSE_DN, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: PPARA activates gene expression; Regulation of lipid metabolism by PPARalpha; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14192](https://www.uniprot.org/uniprotkb/Q14192) (Four and a half LIM domains protein 2):

> May function as a molecular transmitter linking various signaling pathways to transcriptional regulation. Negatively regulates the transcriptional repressor E4F1 and may function in cell growth. Inhibits the transcriptional activity of FOXO1 and its apoptotic function by enhancing the interaction of FOXO1 with SIRT1 and FOXO1 deacetylation. Negatively regulates the calcineurin/NFAT signaling pathway in cardiomyocytes.

**Summary**, from NCBI Gene [2274](https://www.ncbi.nlm.nih.gov/gene/2274):

> This gene encodes a member of the four-and-a-half-LIM-only protein family. Family members contain two highly conserved, tandemly arranged, zinc finger domains with four highly conserved cysteines binding a zinc atom in each zinc finger. This protein is thought to have a role in the assembly of extracellular membranes. Also, this gene is down-regulated during transformation of normal myoblasts to rhabdomyosarcoma cells and the encoded protein may function as a link between presenilin-2 and an …

**Accessions** — [HGNC:3703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3703) · Entrez [2274](https://www.ncbi.nlm.nih.gov/gene/2274) · UniProt [Q14192](https://www.uniprot.org/uniprotkb/Q14192) · Ensembl [ENSG00000115641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115641)

## Data

Gene col 3703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3703); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3703]; `tensor/DDL_lfc|DDL_z.npy` [3703]; `embed/gene_vectors.npy` [3703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3703 or target_col == 3703). Every well: [[FHL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

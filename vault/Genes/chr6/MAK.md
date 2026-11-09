---
symbol: "MAK"
type: "gene"
col: 3289
ensembl_id: "ENSG00000111837"
name: "male germ cell associated kinase"
location: "6p24.2"
module: 14
arm: "+"
pooled_cpm: 12.55
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# MAK

*male germ cell associated kinase* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.46× (z +30.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.840× (z -7.3, q 2e-10, down in 31 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0729×; ⚠ transcription drop; cell-cycle shift, explains ~35% of this change); [[Riluzole hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0509×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.171×); [[Saquinavir (drug)]] 0.5 µM in 1 line (COLO 205 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFATC2]] (+0.64, fdr 7e-06), [[MLF1]] (+0.62, fdr 1e-05), [[MARCKS]] (+0.62, fdr 2e-05); moves opposite to [[IKBKG]] (-0.59, fdr 1e-05), [[POP1]] (-0.58, fdr 1e-05), [[CCT6A]] (-0.58, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CD83]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.46×** | +30.0 | 0e+00 | 46/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **6.34×** | +23.1 | 0e+00 | 47/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.68×** | +17.5 | 0e+00 | 47/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.65×** | +16.2 | 0e+00 | 46/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.41×** | +14.8 | 0e+00 | 44/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +11.2 | 5e-27 | 32/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.96×** | +8.4 | 4e-15 | 42/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +8.0 | 1e-13 | 29/47 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.9 | 2e-13 | 30/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.8 | 4e-13 | 35/48 (SW1417, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.80×** | +7.3 | 1e-11 | 29/45 (BT-474, HT-29, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +7.3 | 1e-11 | 29/40 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +6.0 | 1e-07 | 26/47 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.60×** | +5.7 | 5e-07 | 25/46 (NCI-H460, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +5.4 | 2e-06 | 24/47 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.3 | 5e-06 | 22/47 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +5.0 | 2e-05 | 21/47 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.43×** | +4.5 | 2e-04 | 19/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3289.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0729×; ⚠ transcription drop; cell-cycle shift, explains ~35% of this change); [[Riluzole hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0509×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.171×); [[Saquinavir (drug)]] 0.5 µM in 1 line (COLO 205 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.840× | -7.3 | 2e-10 | 31/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.803×** | -3.9 | 0.033 | 16/48 (RPMI-7951, NCI-H23, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.2 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +21.5) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.171× (z -11.7) |
| [[SW480 (line)]] | alt | 12.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +23.6) | — |
| [[LoVo (line)]] | wt | 10.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +20.0) | — |
| [[PANC-1 (line)]] | alt | 14.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +19.7) | — |
| [[SW1417 (line)]] | alt | 10.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +17.4) | — |
| [[HT-29 (line)]] | alt | 11.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +15.1) | — |
| [[KATO III (line)]] | alt | 7.99 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 15.1× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 8.97 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +20.5) | — |
| [[J82 (line)]] | alt | 16.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +17.2) | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +19.1) | [[Docetaxel (drug)]] 0.05 µM 0.0729× (z -14.2) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 15.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +21.2) | — |
| [[HEC-1-A (line)]] | alt | 9.49 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 8.68 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +9.9) | — |
| [[A-172 (line)]] | wt | 9.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +12.7) | — |
| [[A498 (line)]] | wt | 7.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +13.5) | — |
| [[A549 (line)]] | wt | 16.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +10.8) | — |
| [[C32 (line)]] | wt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +14.0) | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 13.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +15.6) | — |
| [[HS-578T (line)]] | alt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 7.55 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 7.17× (z +8.6) | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0509× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 9.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 35.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 24.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +12.7) | — |
| [[A-427 (line)]] | wt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +17.2) | — |
| [[COLO 205 (line)]] | alt | 9.35 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.111× (z -8.7) |
| [[H4 (line)]] | wt | 8.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 13.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.90× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 7.83 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.34× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 9.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.7) | — |
| [[SW48 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFATC2]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MLF1]] | +0.62 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[MARCKS]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[B2M]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[HLA-A]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[REL]] | +0.59 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PER2]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[OSR2]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LMNA]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CFAP210]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NBPF19]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKBKG]] | -0.59 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[POP1]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.58 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[CDC123]] | -0.58 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[TRAPPC10]] | -0.57 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[NUP50]] | -0.56 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[TRMT12]] | -0.56 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[HERC2P3]] | -0.55 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[NAA50]] | -0.55 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[AHSA1]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CCT3]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[STX16-NPEPL1]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD83]] | C | CD83 activity raises MAK's level | lines that do not express CD83 (4) vs lines expressing it (46) | 1.45× lower at baseline in the lines without CD83 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 1.5); signed map (46.2, 3.0). **Vector** length 78.9, 16.7% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +30.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +14.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.0 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.6 | +7.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.8 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | male germ cell associated kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:10,762,723-10,838,553 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ417M14.2, RP62 |
| Gene groups (HGNC) | CILK1, MAK, MOK protein kinase family |
| Hallmark sets | ANDROGEN_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [P20794](https://www.uniprot.org/uniprotkb/P20794) (Serine/threonine-protein kinase MAK):

> Essential for the regulation of ciliary length and required for the long-term survival of photoreceptors (By similarity). Phosphorylates FZR1 in a cell cycle-dependent manner. Plays a role in the transcriptional coactivation of AR. Could play an important function in spermatogenesis. May play a role in chromosomal stability in prostate cancer cells.

**Summary**, from NCBI Gene [4117](https://www.ncbi.nlm.nih.gov/gene/4117):

> The product of this gene is a serine/threonine protein kinase related to kinases involved in cell cycle regulation. Studies of the mouse and rat homologs have localized the kinase to the chromosomes during meiosis in spermatogenesis, specifically to the synaptonemal complex that exists while homologous chromosomes are paired. Mutations in this gene have been associated with ciliary defects resulting in retinitis pigmentosa 62. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:6816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6816) · Entrez [4117](https://www.ncbi.nlm.nih.gov/gene/4117) · UniProt [P20794](https://www.uniprot.org/uniprotkb/P20794) · Ensembl [ENSG00000111837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111837)

## Data

Gene col 3289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3289); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3289]; `tensor/DDL_lfc|DDL_z.npy` [3289]; `embed/gene_vectors.npy` [3289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3289 or target_col == 3289). Every well: [[MAK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

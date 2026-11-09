---
symbol: "OAS3"
type: "gene"
col: 3221
ensembl_id: "ENSG00000111331"
name: "2'-5'-oligoadenylate synthetase 3"
location: "12q24.13"
module: 32
arm: "+"
pooled_cpm: 100.15
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 53
n_dd_up_clean: 4
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 59
direction_downstream: 84
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# OAS3

*2'-5'-oligoadenylate synthetase 3* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.69× (z +5.4, q 2e-05, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 53 drug-doses (9 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.241× (z -21.5, q 0e+00, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS2]] (+0.95, fdr 7e-06, ⚠ same locus), [[PARP9]] (+0.94, fdr 7e-06), [[CMPK2]] (+0.94, fdr 7e-06), [[STAT1]] (+0.93, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 59 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 84 go from it, the strongest it → [[OAS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +5.4 | 2e-05 | 32/42 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +5.4 | 2e-05 | 29/43 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +4.8 | 3e-04 | 33/42 (KATO III, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.46×** | +3.8 | 0.019 | 29/44 (LS 180, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 1.35× | +3.2 | 0.13 | 22/44 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.35× | +3.1 | 0.13 | 20/42 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.13 | 25/42 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.13 | 20/43 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.33× | +3.1 | 0.13 | 25/43 (A498, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 53 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.241×** | -21.5 | 0e+00 | 34/44 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.181×** | -18.2 | 0e+00 | 41/44 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.331×** | -16.7 | 0e+00 | 37/44 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.272×** | -13.9 | 1e-41 | 37/43 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.274×** | -13.8 | 2e-41 | 36/43 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.288×** | -13.3 | 3e-38 | 36/43 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.312×** | -12.4 | 2e-33 | 37/43 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.317×** | -12.2 | 1e-32 | 35/44 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.465×** | -11.5 | 5e-29 | 34/43 (NCI-H1573, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.389×** | -10.1 | 5e-22 | 38/43 (BT-474, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.385×** | -9.6 | 4e-20 | 39/43 (MIA PaCa-2, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.411×** | -9.1 | 4e-18 | 30/42 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.426×** | -9.1 | 5e-18 | 37/42 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.441×** | -8.7 | 1e-16 | 36/42 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.221×** | -8.4 | 1e-15 | 31/42 (RPMI-7951, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.465×** | -8.1 | 1e-14 | 37/43 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 133 | 0 | 24 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0497× (z -20.7) |
| [[LoVo (line)]] | wt | 256 | 0 | 21 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.173× (z -21.0) |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 21 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0360× (z -21.7) |
| [[SHP-77 (line)]] | alt | 108 | 0 | 21 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0441× (z -20.1) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 20 (6 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.101× (z -21.1) |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 18 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.169× (z -15.4) |
| [[RKO (line)]] | wt | 114 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0656× (z -23.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0874× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 158 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -21.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.162× (z -18.7) |
| [[SNU-423 (line)]] | alt | 134 | 0 | 16 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.186× (z -17.2) |
| [[A-172 (line)]] | wt | 171 | 0 | 15 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.177× (z -19.9) |
| [[A549 (line)]] | wt | 183 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.107× (z -17.7) |
| [[COLO 205 (line)]] | alt | 288 | 0 | 14 | — | [[Panobinostat (drug)]] 0.5 µM 0.0746× (z -17.8) |
| [[RPMI-7951 (line)]] | alt | 186 | 0 | 14 | — | [[Tofacitinib (drug)]] 5 µM 0.158× (z -22.1) |
| [[AsPC-1 (line)]] | alt | 178 | 0 | 13 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.165× (z -18.8) |
| [[NCI-H1792 (line)]] | alt | 87.1 | 0 | 13 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.160× (z -18.2) |
| [[A498 (line)]] | wt | 178 | 0 | 12 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.196× (z -17.0) |
| [[C-33 A (line)]] | alt | 109 | 0 | 12 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0753× (z -16.0) |
| [[KATO III (line)]] | alt | 99.8 | 1 | 11 | [[Harringtonine (drug)]] 0.5 µM 3.28× (z +8.7) | [[Tofacitinib (drug)]] 5 µM 0.238× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 218 | 1 (1 ⚠) | 11 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.81× (z +8.5) ⚠ cell-cycle shift, explains ~61% of this change | [[Tofacitinib (drug)]] 5 µM 0.173× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 185 | 0 | 11 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.165× (z -22.4) |
| [[J82 (line)]] | alt | 109 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 9.27× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Tofacitinib (drug)]] 5 µM 0.326× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.227× (z -14.6) |
| [[SW1417 (line)]] | alt | 158 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.384× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 95.9 | 0 | 6 | — | [[Tofacitinib (drug)]] 5 µM 0.227× (z -15.4) |
| [[SW 900 (line)]] | alt | 65.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.178× (z -11.2) |
| [[C32 (line)]] | wt | 45.8 | 0 | 5 | — | [[Selinexor (drug)]] 5 µM 0.249× (z -11.3) |
| [[HS-578T (line)]] | alt | 33.9 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 0.5 µM 5.60× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.131× (z -11.7) |
| [[PANC-1 (line)]] | alt | 46.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -13.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.428× (z -9.9) |
| [[SNU-1 (line)]] | wt | 60.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.120× (z -9.5) |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.125× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 49.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -10.2) |
| [[Hs 766T (line)]] | wt | 115 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.383× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.72× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 31.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 21.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS2]] | +0.95 | +0.92 / +0.96 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999; ⚠ same locus (1.9 kb, same strand: neighbours can correlate without regulation) |
| [[PARP9]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | STRING 861 |
| [[CMPK2]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 724 |
| [[STAT1]] | +0.93 | +0.92 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 959 |
| [[MX1]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 967 |
| [[USP18]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 910 |
| [[PLSCR1]] | +0.91 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 691 |
| [[TRIM14]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 467 |
| [[IFIT1]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 965 |
| [[OAS1]] | +0.90 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 986; ⚠ same locus (4.8 kb, same strand: neighbours can correlate without regulation) |
| [[RIGI]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 943 |
| [[HERC6]] | +0.90 | +0.86 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 887 |
| [[EIF2AK2]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 959 |
| [[DDX60L]] | +0.89 | +0.82 / +0.93 | both halves | 7e-06 | STRING 533 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 39, C 20. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises OAS3's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.68× lower at baseline in the lines without OAS2 | 5e-05 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[SRMS]] | B | SRMS activity raises OAS3's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.69× lower at baseline in the lines without SRMS | 1e-04 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OAS1]] | B | OAS1 activity raises OAS3's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.60× lower at baseline in the lines without OAS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises OAS3's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.75× lower at baseline in the lines without IFI6 | 8e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises OAS3's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.37× lower at baseline in the lines without CMPK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[BATF2]] | B | BATF2 activity raises OAS3's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.67× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[IFI27]] | B | IFI27 activity raises OAS3's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.66× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[PLSCR1]] | B | PLSCR1 activity raises OAS3's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 3.58× lower at baseline in the lines without PLSCR1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[RASGRP3]] | B | RASGRP3 activity raises OAS3's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises OAS3's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without TRIM22 | 0.004 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[MX1]] | B | MX1 activity raises OAS3's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.85× lower at baseline in the lines without MX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[FBXO39]] | B | FBXO39 activity raises OAS3's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without FBXO39 | 0.004 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 55, C 29. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS3 activity raises OAS1's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 5.74× lower at baseline in the lines without OAS3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[RIGI]] | B | OAS3 activity raises RIGI's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.93× lower at baseline in the lines without OAS3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[PARP14]] | B | OAS3 activity raises PARP14's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 3.53× lower at baseline in the lines without OAS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[OAS2]] | B | OAS3 activity raises OAS2's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 6.17× lower at baseline in the lines without OAS3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[APOL6]] | B | OAS3 activity raises APOL6's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 3.41× lower at baseline in the lines without OAS3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[NLRC5]] | B | OAS3 activity raises NLRC5's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 3.41× lower at baseline in the lines without OAS3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[CMPK2]] | B | OAS3 activity raises CMPK2's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 4.48× lower at baseline in the lines without OAS3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[PARP10]] | B | OAS3 activity raises PARP10's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without OAS3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[SP110]] | B | OAS3 activity raises SP110's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 3.54× lower at baseline in the lines without OAS3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[MYD88]] | B | OAS3 activity raises MYD88's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without OAS3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[TRANK1]] | B | OAS3 activity raises TRANK1's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.87× lower at baseline in the lines without OAS3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[TRIM25]] | B | OAS3 activity raises TRIM25's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without OAS3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.935). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.7, 54.3); signed map (65.1, 32.3). **Vector** length 160, 65.3% of its response variance represented; |z| ≥ 3 in 1,829 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.79 to 56); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.81 to 10); *ISG15 antiviral mechanism* (reactome, mean cos +0.85 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.4 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.5 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +6.0 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +1.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.8 | +2.9 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +4.7 | +3.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -12.5 | -21.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -11.5 | -16.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -10.8 | -13.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -10.2 | -18.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.2 | -12.2 |

## What is on record

|  |  |
|---|---|
| Name | 2'-5'-oligoadenylate synthetase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,938,051-112,976,460 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 2'-5'-oligoadenylate synthetase family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 7 pathways, smallest: OAS antiviral response; IFIT antiviral response; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6K5](https://www.uniprot.org/uniprotkb/Q9Y6K5) (2'-5'-oligoadenylate synthase 3):

> Interferon-induced, dsRNA-activated antiviral enzyme which plays a critical role in cellular innate antiviral response. In addition, it may also play a role in other cellular processes such as apoptosis, cell growth, differentiation and gene regulation. Catalyzes preferentially the dimerization of ATP to form 2'-5'-diadenylate (2-5A), but can also form the trimeric 2'-5'-oligoadenylate. The oligoadenylate then binds to the inactive monomeric form of ribonuclease L (RNase L) leading to its …

**Summary**, from NCBI Gene [4940](https://www.ncbi.nlm.nih.gov/gene/4940):

> This gene encodes an enzyme included in the 2', 5' oligoadenylate synthase family. This enzyme is induced by interferons and catalyzes the 2', 5' oligomers of adenosine in order to bind and activate RNase L. This enzyme family plays a significant role in the inhibition of cellular protein synthesis and viral infection resistance. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8088) · Entrez [4940](https://www.ncbi.nlm.nih.gov/gene/4940) · UniProt [Q9Y6K5](https://www.uniprot.org/uniprotkb/Q9Y6K5) · Ensembl [ENSG00000111331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111331)

## Data

Gene col 3221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3221); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3221]; `tensor/DDL_lfc|DDL_z.npy` [3221]; `embed/gene_vectors.npy` [3221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3221 or target_col == 3221). Every well: [[OAS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OAS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

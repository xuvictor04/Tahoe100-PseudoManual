---
symbol: "MAP3K8"
type: "gene"
col: 2907
ensembl_id: "ENSG00000107968"
name: "mitogen-activated protein kinase kinase kinase 8"
location: "10p11.23"
module: 14
arm: "+"
pooled_cpm: 50.63
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 19
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# MAP3K8

*mitogen-activated protein kinase kinase kinase 8* — 10p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +15.0, q 0e+00, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.500× (z -7.0, q 1e-09, down in 25 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.552× (z -6.9, q 2e-09, down in 31 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (Panc 03.27 0.141×, LoVo 0.239×, AsPC-1 0.229×, HT-29 0.202×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.166×, KATO III 0.191×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.204×, NCI-H2347 0.188×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.418×, LS 180 0.400×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.437×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELF3]] (+0.78, fdr 7e-06), [[EFNA1]] (+0.76, fdr 7e-06), [[ANKRD33B]] (+0.70, fdr 7e-06); moves opposite to [[CLMP]] (-0.53, fdr 1e-05), [[KPNA4]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[RBM47]] → it (grade B ⚠); 5 go from it, the strongest it → [[CLMP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +15.0 | 0e+00 | 30/44 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.11×** | +11.9 | 5e-30 | 42/45 (SNU-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 7e-05 | 25/44 (RKO, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +5.0 | 7e-05 | 23/44 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.0 | 7e-05 | 26/42 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +4.2 | 0.002 | 20/44 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.010 | 17/45 (NCI-H23, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.023 | 17/45 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.026 | 20/44 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.045 | 14/44 (KATO III, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.13 | 14/41 (NCI-H460, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2907.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (Panc 03.27 0.141×, LoVo 0.239×, AsPC-1 0.229×, HT-29 0.202×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.166×, KATO III 0.191×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.204×, NCI-H2347 0.188×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.418×, LS 180 0.400×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.437×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.500×** | -7.0 | 1e-09 | 25/38 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.552×** | -6.9 | 2e-09 | 31/44 (Panc 03.27, LoVo, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.631×** | -5.3 | 2e-05 | 31/43 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.635×** | -5.3 | 2e-05 | 24/41 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.707×** | -4.0 | 0.007 | 22/44 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.713×** | -3.9 | 0.008 | 22/44 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.717×** | -3.8 | 0.010 | 21/44 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.751×** | -3.3 | 0.068 | 19/44 (SW 900, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 133 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.239× (z -13.0) |
| [[HT-29 (line)]] | alt | 145 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 83.2 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.229× (z -11.0) |
| [[LS 180 (line)]] | wt | 76.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 98.6 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.141× (z -14.7) |
| [[KATO III (line)]] | alt | 70.6 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -12.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 41.7 | 4 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +12.4) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 4.07× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 15.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 77.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 38.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +16.5) | — |
| [[NCI-H2347 (line)]] | alt | 64.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -8.7) |
| [[SNU-1 (line)]] | wt | 110 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +11.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.437× (z -9.4) |
| [[BT-474 (line)]] | alt | 57.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -10.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 64.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 43.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.9× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 37.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 7.88× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 32.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +15.4) | — |
| [[SW 900 (line)]] | alt | 52.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.196× (z -8.8) |
| [[A-172 (line)]] | wt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +13.1) | — |
| [[A498 (line)]] | wt | 57.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +13.8) | — |
| [[A549 (line)]] | wt | 72.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +17.6) | — |
| [[Hs 766T (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -11.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.65× (z +9.3) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 49.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 8.77× (z +8.5) ⚠ toxic | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 1 | — | [[IQ 1 (drug)]] 0.05 µM 0.0617× (z -8.5) |
| [[A-427 (line)]] | wt | 7.73 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF3]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[EFNA1]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ANKRD33B]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PIK3C2B]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[IRF1]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING |
| [[PLAAT3]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TMPRSS3]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SMAD7]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RHOV]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CXCL3]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLMP]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM47]] | B | RBM47 activity raises MAP3K8's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without RBM47 | 0.003 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[PRR15]] | B | PRR15 activity raises MAP3K8's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without PRR15 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[GATA6]] | B | GATA6 activity raises MAP3K8's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without GATA6 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[CLIC5]] | B | CLIC5 activity raises MAP3K8's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.29× lower at baseline in the lines without CLIC5 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[TRIM31]] | B | TRIM31 activity raises MAP3K8's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.62× lower at baseline in the lines without TRIM31 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[FRMD4B]] | B | FRMD4B activity raises MAP3K8's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without FRMD4B | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[RHOV]] | B | RHOV activity raises MAP3K8's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without RHOV | 0.021 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises MAP3K8's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.38× lower at baseline in the lines without TMPRSS2 | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[GBP2]] | B | GBP2 activity raises MAP3K8's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without GBP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[CXCL3]] | B | CXCL3 activity raises MAP3K8's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without CXCL3 | 0.028 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[TJP2]] | B | TJP2 activity raises MAP3K8's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without TJP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[PLEKHG6]] | B | PLEKHG6 activity raises MAP3K8's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without PLEKHG6 | 0.031 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLMP]] | C | MAP3K8 activity raises CLMP's level | lines that do not express MAP3K8 (4) vs lines expressing it (46) | 4.77× lower at baseline in the lines without MAP3K8 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, LINC02656, SOX9; maybe low, not absent; its own permutation p |
| [[CXCL3]] | C | MAP3K8 activity raises CXCL3's level | lines that do not express MAP3K8 (4) vs lines expressing it (46) | 4.68× lower at baseline in the lines without MAP3K8 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, LINC02656, SOX9; maybe low, not absent; its own permutation p |
| [[NFKBIA]] | C | MAP3K8 activity raises NFKBIA's level | lines that do not express MAP3K8 (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without MAP3K8 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, LINC02656, SOX9; maybe low, not absent; its own permutation p |
| [[TNIP1]] | C | MAP3K8 activity raises TNIP1's level | lines that do not express MAP3K8 (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without MAP3K8 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, LINC02656, SOX9; maybe low, not absent |
| [[GATA6]] | C | MAP3K8 activity raises GATA6's level | lines that do not express MAP3K8 (4) vs lines expressing it (46) | 3.82× lower at baseline in the lines without MAP3K8 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, LINC02656, SOX9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.3, 3.8); signed map (45.7, 6.5). **Vector** length 148, 47.7% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +15.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.4 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.3 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.1 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.7 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.23 — chr10:30,434,021-30,461,833 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Tpl-2, EST, c-COT, MEKK8; previously COT, ESTF |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE-unique family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 28 pathways, smallest: MAP3K8 (TPL2)-dependent MAPK1/3 activation; CD28 dependent PI3K/Akt signaling; Co-stimulation by CD28 |
| Matched by | ensembl_id |

**Function**, from UniProt [P41279](https://www.uniprot.org/uniprotkb/P41279) (Mitogen-activated protein kinase kinase kinase 8):

> Required for lipopolysaccharide (LPS)-induced, TLR4-mediated activation of the MAPK/ERK pathway in macrophages, thus being critical for production of the pro-inflammatory cytokine TNF (TNF) during immune responses. Involved in the regulation of T-helper cell differentiation and IFNG expression in T-cells. Involved in mediating host resistance to bacterial infection through negative regulation of type I interferon (IFN) production. In vitro, activates MAPK/ERK pathway in response to IL1 in an …

**Summary**, from NCBI Gene [1326](https://www.ncbi.nlm.nih.gov/gene/1326):

> This gene is an oncogene that encodes a member of the serine/threonine protein kinase family. The encoded protein localizes to the cytoplasm and can activate both the MAP kinase and JNK kinase pathways. This protein was shown to activate IkappaB kinases, and thus induce the nuclear production of NF-kappaB. This protein was also found to promote the production of TNF-alpha and IL-2 during T lymphocyte activation. This gene may also utilize a downstream in-frame translation start codon, and thus …

**Accessions** — [HGNC:6860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6860) · Entrez [1326](https://www.ncbi.nlm.nih.gov/gene/1326) · UniProt [P41279](https://www.uniprot.org/uniprotkb/P41279) · Ensembl [ENSG00000107968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107968)

## Data

Gene col 2907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2907); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2907]; `tensor/DDL_lfc|DDL_z.npy` [2907]; `embed/gene_vectors.npy` [2907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2907 or target_col == 2907). Every well: [[MAP3K8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

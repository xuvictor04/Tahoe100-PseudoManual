---
symbol: "AGAP4"
type: "gene"
col: 11993
ensembl_id: "ENSG00000188234"
name: "ArfGAP with GTPase domain, ankyrin repeat and PH domain 4"
location: "10q11.22"
module: 5
arm: "+"
pooled_cpm: 6.05
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# AGAP4

*ArfGAP with GTPase domain, ankyrin repeat and PH domain 4* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.55× (z +6.3, q 1e-07, up in 18 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +6.2, q 1e-07, up in 17 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.729× (z -4.5, q 0.003, down in 16 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Asciminib (drug)]] 0.05 µM: 0.788× (z -3.4, q 0.095, down in 9 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 0.0325×, SW480 0.236×, SNU-423 0.0889×, LS 180 0.159×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Omeprazole (drug)]] 0.5 µM in 1 line (A-172 0.0938×); [[Talc (drug)]] 0.05 µM in 1 line (NCI-H23 0.127×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRD4]] (+0.61, fdr 1e-05), [[PARGP1]] (+0.60, fdr 1e-05, ⚠ same locus), [[NPIPB12]] (+0.60, fdr 2e-05), [[AGAP6]] (+0.59, fdr 1e-05); moves opposite to [[ENPP1]] (-0.54, fdr 2e-04), [[AMOT]] (-0.54, fdr 4e-05), [[CSRP1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.55×** | +6.3 | 1e-07 | 18/47 (SW480, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.2 | 1e-07 | 17/39 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.0 | 5e-07 | 17/39 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +5.9 | 5e-07 | 17/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.8 | 6e-07 | 10/48 (A-427, LOX-IMVI, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +5.6 | 2e-06 | 11/41 (A498, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.2 | 2e-05 | 18/43 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.42×** | +5.0 | 3e-05 | 14/46 (SW480, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.9 | 5e-05 | 9/23 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.38×** | +4.6 | 3e-04 | 10/45 (A-172, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.003 | 6/47 (A498, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.022 | 6/44 (NCI-H23, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.5 | 0.023 | 5/46 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.036 | 3/44 (CFPAC-1, SW 900, …) | rises with dose | position effect removed |
| [[Idoxuridine (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.042 | 5/44 (A-172, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11993.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 0.0325×, SW480 0.236×, SNU-423 0.0889×, LS 180 0.159×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Omeprazole (drug)]] 0.5 µM in 1 line (A-172 0.0938×); [[Talc (drug)]] 0.05 µM in 1 line (NCI-H23 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.729×** | -4.5 | 0.003 | 16/29 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.764×** | -3.4 | 0.095 | 16/44 (RKO, RPMI-7951, …) | rises with dose | composition shift |
| [[Asciminib (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.095 | 9/45 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.095 | 10/43 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.798× | -3.2 | 0.13 | 11/44 (SW480, HS-578T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.07 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0325× (z -25.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.38 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0938× (z -10.7) |
| [[A498 (line)]] | wt | 3.91 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -10.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HT-29 (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.66 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.52 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.127× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 8.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 9.44 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0703× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 6.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0889× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 9.91 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRD4]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[PARGP1]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 | ⚠ same locus (34.3 kb, same strand: neighbours can correlate without regulation) |
| [[NPIPB12]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[AGAP6]] | +0.59 | +0.65 / +0.53 | both halves | 1e-05 | same gene group; STRING 925 |
| [[AGAP5]] | +0.59 | +0.65 / +0.58 | both halves | 7e-06 | same gene group; STRING 538 |
| [[TIMM23B-AGAP6]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HIRA]] | +0.59 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[VPS53]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[NPIPB11]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ORC2]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TRAPPC12]] | +0.57 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[UBE3C]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[LARS2]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENPP1]] | -0.54 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[AMOT]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[CSRP1]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[GMFB]] | -0.52 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[EMD]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ISOC1]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[JUNB]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[TBL1XR1]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SUGT1P3]] | -0.49 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[TEX261]] | -0.49 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[TP53INP2]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TUFT1]] | -0.48 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AGAP4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MTHFD1L]] | C | MTHFD1L activity raises AGAP4's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.42× lower at baseline in the lines without MTHFD1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (20.5, -14.1); signed map (3.5, -54.5). **Vector** length 51.7, 6.34% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.3 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.4 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.2 | -0.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with GTPase domain, ankyrin repeat and PH domain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:45,825,594-45,853,875 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Em:AC012044.1, MRIP2; previously CTGLF1, AGAP8, CTGLF5 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P64](https://www.uniprot.org/uniprotkb/Q96P64) (Arf-GAP with GTPase, ANK repeat and PH domain-containing protein 4):

> Putative GTPase-activating protein.

**Summary**, from NCBI Gene [119016](https://www.ncbi.nlm.nih.gov/gene/119016):

> Predicted to enable GTPase activator activity and GTPase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23459) · Entrez [119016](https://www.ncbi.nlm.nih.gov/gene/119016) · UniProt [Q96P64](https://www.uniprot.org/uniprotkb/Q96P64) · Ensembl [ENSG00000188234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188234)

## Data

Gene col 11993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11993); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11993]; `tensor/DDL_lfc|DDL_z.npy` [11993]; `embed/gene_vectors.npy` [11993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11993 or target_col == 11993). Every well: [[AGAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

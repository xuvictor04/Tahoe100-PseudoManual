---
symbol: "SNRNP35"
type: "gene"
col: 11505
ensembl_id: "ENSG00000184209"
name: "small nuclear ribonucleoprotein U11/U12 subunit 35"
location: "12q24.31"
module: 114
arm: "+"
pooled_cpm: 14.86
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# SNRNP35

*small nuclear ribonucleoprotein U11/U12 subunit 35* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.24× (z +5.0, q 3e-04, up in 18 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM: 1.24× (z +3.6, q 0.051, up in 5 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.566× (z -9.0, q 1e-16, down in 30 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Gefitinib (drug)]] 5 µM: 0.806× (z -3.6, q 0.021, down in 6 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.158×, MIA PaCa-2 0.169×, LoVo 0.255×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.130×, MIA PaCa-2 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.281×, SNU-423 0.338×; ⚠ cell-cycle shift, explains ~25% of this change); [[Silodosin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0807×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.135×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (SW48 0.0854×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEFM]] (+0.68, fdr 7e-06), [[GMEB2]] (+0.64, fdr 1e-05), [[ZNF707]] (+0.63, fdr 7e-06); moves opposite to [[TKT]] (-0.51, fdr 6e-05), [[BZW2]] (-0.51, fdr 3e-05), [[AZIN1]] (-0.50, fdr 3e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC16A1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.24×** | +5.0 | 3e-04 | 18/48 (LOX-IMVI, LoVo, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.8 | 0.037 | 15/41 (KATO III, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.051 | 5/47 (SW480, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.22× | +3.3 | 0.13 | 6/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.22× | +3.2 | 0.13 | 17/46 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.17 | 6/44 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.21 | 5/48 (LOX-IMVI, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11505.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (CFPAC-1 0.158×, MIA PaCa-2 0.169×, LoVo 0.255×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.130×, MIA PaCa-2 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.281×, SNU-423 0.338×; ⚠ cell-cycle shift, explains ~25% of this change); [[Silodosin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0807×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.135×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (SW48 0.0854×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -9.0 | 1e-16 | 30/42 (hTERT-HPNE, SNU-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.617×** | -8.0 | 4e-13 | 33/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.625×** | -7.8 | 1e-12 | 22/38 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.674×** | -6.5 | 9e-09 | 23/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.702×** | -5.9 | 5e-07 | 28/47 (LS 180, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.720×** | -5.2 | 2e-05 | 19/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.803×** | -5.1 | 2e-05 | 22/47 (AsPC-1, SNU-423, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.783×** | -3.9 | 0.008 | 18/46 (SW48, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.856× | -3.6 | 0.017 | 20/46 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.021 | 6/48 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Aliskiren (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.031 | 11/48 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.800×** | -3.4 | 0.031 | 8/31 (HT-29, C32, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.817× | -3.0 | 0.12 | 7/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 9.25 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0807× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.135× (z -9.5) |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0827× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[LoVo (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.157× (z -8.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0854× (z -9.3) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEFM]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[GMEB2]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ZNF707]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[EXO5-DT]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ZNF493]] | +0.62 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TIMM29]] | +0.61 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[MIR762HG]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[COA5]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TRIM13]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PIGC]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TKT]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[BZW2]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[AZIN1]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[FOSB]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[VDAC1]] | -0.49 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[TLN1]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[VPS13A]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ANXA2]] | -0.48 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[IPO7]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A1]] | C | SLC16A1 activity lowers SNRNP35's level | lines that do not express SLC16A1 (3) vs lines expressing it (47) | 1.44× higher at baseline in the lines without SLC16A1 | 0.098 | ⚠ few lines (3 vs 47); across organs; co-occurs with ERBB2; also absent: SLC16A1-AS1, SLC4A7, PALS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.9, 16.1); signed map (-9.3, -14.8). **Vector** length 69.5, 11.5% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.5 | -5.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -1.7 | -7.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein U11/U12 subunit 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,458,088-123,473,154 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U1SNRNPBP |
| Gene groups (HGNC) | RNA binding motif containing; U11/U12 di-snRNP; U11 small nuclear ribonucleoprotein |
| Reactome | 4 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

UniProt [Q16560](https://www.uniprot.org/uniprotkb/Q16560) carries no function annotation.

**Summary**, from NCBI Gene [11066](https://www.ncbi.nlm.nih.gov/gene/11066):

> The protein encoded by this gene is a homolog of the U1-snRNP binding protein. The N-terminal half contains a RNA recognition motif and the C-terminal half is rich in Arg/Asp and Arg/Glu dipeptides, which is a characteristic of a variety of splicing factors. This protein is a component of the U11/U12 small nuclear ribonucleoproteins (snRNP) that form part of the U12-type spliceosome. Alternative splicing results in multiple transcript variants encoding two distinct isoforms and representing a …

**Accessions** — [HGNC:30852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30852) · Entrez [11066](https://www.ncbi.nlm.nih.gov/gene/11066) · UniProt [Q16560](https://www.uniprot.org/uniprotkb/Q16560) · Ensembl [ENSG00000184209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184209)

## Data

Gene col 11505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11505); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11505]; `tensor/DDL_lfc|DDL_z.npy` [11505]; `embed/gene_vectors.npy` [11505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11505 or target_col == 11505). Every well: [[SNRNP35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRNP35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

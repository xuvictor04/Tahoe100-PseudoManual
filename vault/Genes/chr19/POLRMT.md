---
symbol: "POLRMT"
type: "gene"
col: 1818
ensembl_id: "ENSG00000099821"
name: "RNA polymerase mitochondrial"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 13.66
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# POLRMT

*RNA polymerase mitochondrial* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.51× (z +5.8, q 5e-06, up in 26 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.44× (z +5.1, q 1e-04, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.656× (z -8.3, q 4e-14, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLX9]] (+0.79, fdr 7e-06), [[BRF1]] (+0.73, fdr 1e-05), [[TRABD]] (+0.71, fdr 1e-05); moves opposite to [[TSGA10]] (-0.64, fdr 3e-04), [[EFCAB5]] (-0.63, fdr 4e-04), [[PPP1R12A-AS2]] (-0.63, fdr 5e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.8 | 5e-06 | 26/46 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +5.1 | 1e-04 | 22/46 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.42×** | +4.9 | 2e-04 | 24/46 (SW480, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +4.8 | 2e-04 | 23/46 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +4.6 | 6e-04 | 18/46 (SW480, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.36×** | +4.4 | 0.001 | 15/39 (NCI-H460, LoVo, …) | two highest doses | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.33×** | +3.9 | 0.008 | 18/43 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.008 | 13/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.009 | 14/43 (HT-29, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.032 | 13/44 (NCI-H460, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.29×** | +3.4 | 0.032 | 10/25 (A498, SNU-423, …) | two highest doses | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.045 | 16/46 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.055 | 11/44 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.25×** | +3.2 | 0.058 | 12/41 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.2 | 0.058 | 7/31 (RKO, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.065 | 5/47 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.089 | 12/46 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.089 | 8/45 (LS 180, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -8.3 | 4e-14 | 34/46 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.696×** | -7.2 | 2e-10 | 26/47 (A498, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.701×** | -7.0 | 4e-10 | 28/46 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -5.9 | 5e-07 | 22/44 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -5.6 | 3e-06 | 20/45 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -4.8 | 1e-04 | 20/46 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.011 | 18/47 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -3.5 | 0.030 | 18/47 (A498, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.786×** | -3.4 | 0.046 | 14/46 (SNU-1, HCT15, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.787×** | -3.3 | 0.046 | 7/46 (SW480, A-172, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.797×** | -3.2 | 0.078 | 8/46 (NCI-H460, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 25.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -12.1) |
| [[A-427 (line)]] | wt | 26.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -15.2) |
| [[RKO (line)]] | wt | 22.2 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0977× (z -13.5) |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.2) |
| [[A498 (line)]] | wt | 15.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.447× (z -8.5) |
| [[A549 (line)]] | wt | 18.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 9.29 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.5) |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0922× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLX9]] | +0.79 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[BRF1]] | +0.73 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TRABD]] | +0.71 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.71 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[E2F4]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[NLE1]] | +0.70 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[IMPDH1]] | +0.69 | +0.64 / +0.51 | both halves | 1e-05 | STRING 461 |
| [[RSAD1]] | +0.68 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[TMEM201]] | +0.68 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CPSF1]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ZNF692]] | +0.68 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[DPH7]] | +0.68 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSGA10]] | -0.64 | -0.65 / -0.29 | both halves | 3e-04 |  |
| [[EFCAB5]] | -0.63 | -0.62 / -0.26 | both halves | 4e-04 |  |
| [[PPP1R12A-AS2]] | -0.63 | -0.61 / -0.23 | both halves | 5e-04 |  |
| [[WAC-AS1]] | -0.62 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[ERCC6L2-AS1]] | -0.61 | -0.60 / -0.24 | both halves | 5e-04 |  |
| [[KANSL1L]] | -0.61 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[IFNAR1]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[LINC00571]] | -0.60 | -0.57 / -0.26 | both halves | 3e-04 |  |
| [[MR1]] | -0.59 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[MMADHC-DT]] | -0.59 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[ZNF341-AS1]] | -0.59 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[AHI1-DT]] | -0.59 | -0.57 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises POLRMT's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.65× lower at baseline in the lines without GNAZ | 0.036 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises POLRMT's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.3, -26.3); signed map (-42.7, -9.8). **Vector** length 83.2, 16.2% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.1 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.0 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.9 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:617,221-633,537 (-) |
| Ensembl biotype | protein_coding |
| Also known as | h-mtRPOL, APOLMT, MTRNAP, MTRPOL |
| Gene groups (HGNC) | Pentatricopeptide repeat containing; Mitochondrial transcription initiation complex subunits |
| Reactome | 6 pathways, smallest: Mitochondrial transcription; Strand-asynchronous mitochondrial DNA replication; Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O00411](https://www.uniprot.org/uniprotkb/O00411) (DNA-directed RNA polymerase, mitochondrial):

> DNA-dependent RNA polymerase catalyzes the transcription of mitochondrial DNA into RNA using the four ribonucleoside triphosphates as substrates. Component of the mitochondrial transcription initiation complex, composed at least of TFB2M, TFAM and POLRMT that is required for basal transcription of mitochondrial DNA. In this complex, TFAM recruits POLRMT to a specific promoter whereas TFB2M induces structural changes in POLRMT to enable promoter opening and trapping of the DNA non-template …

**Summary**, from NCBI Gene [5442](https://www.ncbi.nlm.nih.gov/gene/5442):

> This gene encodes a mitochondrial DNA-directed RNA polymerase. The gene product is responsible for mitochondrial gene expression as well as for providing RNA primers for initiation of replication of the mitochondrial genome. Although this polypeptide has the same function as the three nuclear DNA-directed RNA polymerases, it is more closely related to RNA polymerases of phage and mitochondrial polymerases of lower eukaryotes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9200) · Entrez [5442](https://www.ncbi.nlm.nih.gov/gene/5442) · UniProt [O00411](https://www.uniprot.org/uniprotkb/O00411) · Ensembl [ENSG00000099821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099821)

## Data

Gene col 1818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1818); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1818]; `tensor/DDL_lfc|DDL_z.npy` [1818]; `embed/gene_vectors.npy` [1818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1818 or target_col == 1818). Every well: [[POLRMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLRMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

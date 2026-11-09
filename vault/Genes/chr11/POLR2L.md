---
symbol: "POLR2L"
type: "gene"
col: 10856
ensembl_id: "ENSG00000177700"
name: "RNA polymerase II, I and III subunit L"
location: "11p15.5"
module: 63
arm: "+"
pooled_cpm: 41.79
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# POLR2L

*RNA polymerase II, I and III subunit L* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.80× (z +10.0, q 9e-21, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +7.5, q 1e-11, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Silodosin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0822×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFN1]] (+0.63, fdr 1e-05), [[S100A6]] (+0.63, fdr 1e-05), [[S100A10]] (+0.62, fdr 1e-05); moves opposite to [[GPN1]] (-0.64, fdr 7e-06), [[SHMT2]] (-0.61, fdr 2e-05), [[NARS1]] (-0.61, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **5.80×** | +10.0 | 9e-21 | 46/46 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **4.13×** | +8.1 | 2e-13 | 47/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **4.36×** | +8.0 | 2e-13 | 36/36 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +7.5 | 1e-11 | 45/47 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **3.28×** | +6.7 | 2e-09 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.92×** | +6.1 | 1e-07 | 47/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.55×** | +5.3 | 9e-06 | 46/48 (COLO 205, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.59×** | +5.2 | 2e-05 | 42/48 (J82, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **3.24×** | +5.1 | 2e-05 | 37/42 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +5.0 | 3e-05 | 40/45 (MIA PaCa-2, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.34×** | +4.8 | 7e-05 | 40/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **2.27×** | +4.6 | 2e-04 | 41/48 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.5 | 2e-04 | 42/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.77×** | +4.5 | 2e-04 | 33/47 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **2.19×** | +4.4 | 3e-04 | 41/46 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.98×** | +3.7 | 0.005 | 42/48 (J82, LS 180, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **3.07×** | +3.5 | 0.011 | 42/48 (HEC-1-A, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.79×** | +3.3 | 0.025 | 34/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.79×** | +3.2 | 0.028 | 39/48 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.50×** | +2.9 | 0.085 | 26/46 (HCT15, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10856.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Silodosin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0822×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tadalafil (drug)]] 5 µM |  | 0.581× | -3.0 | 0.63 | 33/48 (HepG2/C3A, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.92 per unit of S-phase module lfc, +0.84 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 36.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.8× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[PANC-1 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.77× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW480 (line)]] | alt | 29.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.79× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A-172 (line)]] | wt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A549 (line)]] | wt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.81× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[C32 (line)]] | wt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.71× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0822× (z -8.7) |
| [[HOP62 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.46× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[HT-29 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.99× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H460 (line)]] | wt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.49× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[Panc 03.27 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[RPMI-7951 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.08× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW 900 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.62× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A-427 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[S100A6]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[S100A10]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NDUFA3]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | +0.61 | +0.51 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB3]] | +0.59 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[COX7B]] | +0.59 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[POLR2K]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 | same gene group; pathway: Abortive elongation of HIV-1 transcript in the absence of Tat; STRING 999 |
| [[COPS9]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 | STRING 502 |
| [[MIF]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[TNRC6C]] | +0.55 | +0.59 / +0.54 | both halves | 1e-05 | pathway: ESR-mediated signaling; STRING 562 |
| [[LRCH3]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[COX17]] | +0.54 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN1]] | -0.64 | -0.61 / -0.62 | both halves | 7e-06 | STRING 648 |
| [[SHMT2]] | -0.61 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[NARS1]] | -0.61 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[XPOT]] | -0.60 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[CHORDC1]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TCEA1]] | -0.58 | -0.64 / -0.53 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins; STRING 986 |
| [[TCP1]] | -0.58 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[ZW10]] | -0.58 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[UBQLN1]] | -0.58 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[HSPA9]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[RSL24D1]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[OTULIN]] | -0.56 | -0.68 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLR2L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction -0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.2, 41.9); signed map (45.6, -4.3). **Vector** length 77.6, 31.9% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +5.2 | +8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.8 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +4.4 | +4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.6 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.4 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -0.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II, I and III subunit L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:837,356-842,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPB10beta, RBP10, RPABC5, RPB7.6, hRPB7.6, hsRPB10b |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 94 pathways, smallest: RNA Polymerase III Chain Elongation; Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P62875](https://www.uniprot.org/uniprotkb/P62875) (DNA-directed RNA polymerases I, II, and III subunit RPABC5):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Common component of RNA polymerases I, II and III which synthesize ribosomal RNA precursors, mRNA precursors and many functional non-coding RNAs, and a small RNAs, such as 5S rRNA and tRNAs, respectively.

**Summary**, from NCBI Gene [5441](https://www.ncbi.nlm.nih.gov/gene/5441):

> This gene encodes a subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains four conserved cysteines characteristic of an atypical zinc-binding domain. Like its counterpart in yeast, this subunit may be shared by the other two DNA-directed RNA polymerases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9199) · Entrez [5441](https://www.ncbi.nlm.nih.gov/gene/5441) · UniProt [P62875](https://www.uniprot.org/uniprotkb/P62875) · Ensembl [ENSG00000177700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177700)

## Data

Gene col 10856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10856); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10856]; `tensor/DDL_lfc|DDL_z.npy` [10856]; `embed/gene_vectors.npy` [10856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10856 or target_col == 10856). Every well: [[POLR2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

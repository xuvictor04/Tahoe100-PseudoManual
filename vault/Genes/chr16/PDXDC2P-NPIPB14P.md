---
symbol: "PDXDC2P-NPIPB14P"
type: "gene"
col: 12268
ensembl_id: "ENSG00000196696"
name: "PDXDC2P-NPIPB14P readthrough, transcribed pseudogene"
location: "16q22.1"
module: 56
arm: "+"
pooled_cpm: 16.92
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PDXDC2P-NPIPB14P

*PDXDC2P-NPIPB14P readthrough, transcribed pseudogene* — 16q22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.373× (z -12.8, q 1e-34, down in 24 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.464× (z -10.4, q 1e-22, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXDC2P]] (+0.92, fdr 7e-06, ⚠ same locus), [[PDXDC1]] (+0.91, fdr 7e-06), [[NPIPB14P]] (+0.81, fdr 7e-06, ⚠ same locus), [[KDELR2]] (+0.75, fdr 7e-06), [[EIF2AK3]] (+0.74, fdr 7e-06); moves opposite to [[ZNF300]] (-0.61, fdr 1e-05), [[C7orf25]] (-0.56, fdr 1e-05), [[ZNF239]] (-0.56, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CADPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12268.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.373×** | -12.8 | 1e-34 | 24/30 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.464×** | -10.4 | 1e-22 | 37/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.504×** | -9.2 | 5e-18 | 28/37 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -8.1 | 9e-14 | 28/44 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.551×** | -7.7 | 1e-12 | 27/40 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.590×** | -7.1 | 1e-10 | 29/47 (A498, HS-578T, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -6.8 | 6e-10 | 30/47 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.604×** | -6.3 | 2e-08 | 20/33 (HS-578T, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.720×** | -6.2 | 3e-08 | 26/48 (HS-578T, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.631×** | -6.2 | 3e-08 | 26/44 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.631×** | -6.0 | 1e-07 | 27/47 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.666×** | -5.5 | 2e-06 | 26/47 (A498, HOP62, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.751×** | -5.4 | 2e-06 | 25/47 (HS-578T, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.687×** | -4.9 | 5e-05 | 20/44 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -4.5 | 3e-04 | 20/47 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -4.1 | 0.001 | 19/46 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.721×** | -4.1 | 0.001 | 16/43 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -4.0 | 0.002 | 22/47 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.745×** | -4.0 | 0.002 | 19/44 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.666×** | -3.7 | 0.006 | 15/45 (AN3 CA, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.011 | 16/47 (HT-29, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.844× | -3.2 | 0.026 | 12/48 (H4, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 36.8 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.196× (z -13.7) |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0610× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.293× (z -11.6) |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.216× (z -10.3) |
| [[SW480 (line)]] | alt | 25.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0812× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 7.29 | 0 | 2 | — | [[Drospirenone (drug)]] 0.5 µM 0.0592× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -9.6) |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 2 (1 ⚠) | — | [[Cilostazol (drug)]] 0.05 µM 0.0386× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 2 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0761× (z -10.3) |
| [[HT-29 (line)]] | alt | 29.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0718× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.136× (z -9.1) |
| [[KATO III (line)]] | alt | 25.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Isocorydine (drug)]] 0.5 µM 0.155× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -9.7) |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0865× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW48 (line)]] | wt | 16.5 | 0 | 2 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0628× (z -11.7) |
| [[A-172 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0523× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0741× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXDC2P]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PDXDC1]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[NPIPB14P]] | +0.81 | +0.76 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[KDELR2]] | +0.75 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[COG6]] | +0.72 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[MCEE]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.69 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[ARFGAP3]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SLC25A42]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF300]] | -0.61 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[C7orf25]] | -0.56 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ZNF239]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADPS2]] | B | CADPS2 activity raises PDXDC2P-NPIPB14P's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without CADPS2 | 0.026 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[TOP2A]] | B | TOP2A activity raises PDXDC2P-NPIPB14P's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPIPB14P]] | C | NPIPB14P's natural level strengthens PDXDC2P-NPIPB14P's drug response | NPIPB14P's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.53; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, -34.1); signed map (-49.8, 10.7). **Vector** length 83.4, 17.3% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.60 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.60 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.60 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.2 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.0 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +1.9 | -5.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.4 | +0.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Elimusertib hydrochloride (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | PDXDC2P-NPIPB14P readthrough, transcribed pseudogene |
| Locus type | readthrough (other) |
| Location | 16q22.1 — chr16:69,976,297-70,065,948 (-) |
| Ensembl biotype | lncRNA |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [283970](https://www.ncbi.nlm.nih.gov/gene/283970):

> This locus represents naturally-occurring readthrough transcription between two pseudogenes, PDXDC2P (pyridoxal dependent decarboxylase domain containing 2, pseudogene) and NPIPB14P (nuclear pore complex interacting protein family, member B14, pseudogene). The individual pseudogene loci are not curated as transcribed regions. Readthrough transcripts likely do not encode functional proteins. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:53158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53158) · Entrez [283970](https://www.ncbi.nlm.nih.gov/gene/283970) · Ensembl [ENSG00000196696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196696)

## Data

Gene col 12268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12268); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12268]; `tensor/DDL_lfc|DDL_z.npy` [12268]; `embed/gene_vectors.npy` [12268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12268 or target_col == 12268). Every well: [[PDXDC2P-NPIPB14P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDXDC2P-NPIPB14P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

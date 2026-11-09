---
symbol: "KDELR3"
type: "gene"
col: 1886
ensembl_id: "ENSG00000100196"
name: "KDEL endoplasmic reticulum protein retention receptor 3"
location: "22q13.1"
module: 56
arm: "+"
pooled_cpm: 21.87
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 39
n_dd_up_clean: 4
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# KDELR3

*KDEL endoplasmic reticulum protein retention receptor 3* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[XRK3F2 (drug)]] 0.5 µM: 1.52× (z +4.3, q 0.012, up in 18 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.239× (z -28.7, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDELR2]] (+0.81, fdr 7e-06), [[COG6]] (+0.78, fdr 7e-06), [[SEC13]] (+0.75, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); 15 go from it, the strongest it → cells under [[Glycyrrhizic acid (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 0.012 | 18/42 (HEC-1-A, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.014 | 18/43 (hTERT-HPNE, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.018 | 14/44 (NCI-H2347, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.038 | 9/45 (KATO III, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.26× | +3.2 | 0.14 | 12/32 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.24× | +3.1 | 0.14 | 14/38 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.24× | +3.1 | 0.14 | 15/45 (LS 180, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.239×** | -28.7 | 0e+00 | 43/44 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.216×** | -19.4 | 0e+00 | 40/43 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.254×** | -18.7 | 0e+00 | 40/44 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.378×** | -13.8 | 2e-41 | 42/45 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.418×** | -12.4 | 3e-33 | 37/44 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -12.0 | 5e-31 | 34/43 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.463×** | -10.9 | 6e-26 | 39/45 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -10.2 | 1e-22 | 35/44 (AsPC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.494×** | -10.0 | 1e-21 | 38/45 (HCT15, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -10.0 | 1e-21 | 35/45 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.529×** | -9.0 | 9e-18 | 34/45 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.544×** | -8.6 | 3e-16 | 32/45 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.534×** | -8.4 | 2e-15 | 33/44 (SW48, RPMI-7951, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.557×** | -8.3 | 4e-15 | 35/45 (C32, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.331×** | -8.2 | 8e-15 | 31/45 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.665×** | -8.2 | 1e-14 | 35/45 (H4, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 39.1 | 0 | 13 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0487× (z -15.7) |
| [[HS-578T (line)]] | alt | 75.9 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -25.7) |
| [[RPMI-7951 (line)]] | alt | 33.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0603× (z -24.0) |
| [[NCI-H1792 (line)]] | alt | 28.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0344× (z -18.7) |
| [[A-172 (line)]] | wt | 19.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.8) |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0673× (z -27.3) |
| [[Hs 766T (line)]] | wt | 51.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -24.8) |
| [[hTERT-HPNE (line)]] | wt | 46.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.4) |
| [[LoVo (line)]] | wt | 32.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 9.42 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.6) |
| [[C32 (line)]] | wt | 21.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0282× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.176× (z -13.5) |
| [[KATO III (line)]] | alt | 39.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -21.3) |
| [[SNU-1 (line)]] | wt | 46.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.8) |
| [[A549 (line)]] | wt | 15.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -19.0) |
| [[A498 (line)]] | wt | 53.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -29.6) |
| [[J82 (line)]] | alt | 17.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.187× (z -13.1) |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -8.7) |
| [[SW48 (line)]] | wt | 64.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -19.1) |
| [[SW480 (line)]] | alt | 16.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.0) |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.3) |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0726× (z -12.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -10.7) |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.2) |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.6) |
| [[A-427 (line)]] | wt | 10.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -8.5) |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.3) |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 7.06 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.128× (z -8.7) |
| [[RKO (line)]] | wt | 9.85 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0730× (z -9.8) |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR2]] | +0.81 | +0.82 / +0.76 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 922 |
| [[COG6]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC13]] | +0.75 | +0.73 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC31A]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[CALU]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 455 |
| [[MANF]] | +0.72 | +0.69 / +0.61 | both halves | 7e-06 | STRING 516 |
| [[PDXDC1]] | +0.72 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[COPB1]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 673 |
| [[SLC31A1]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[SUCO]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity raises KDELR3's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without SLC1A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[SNHG18]] | B | SNHG18 activity raises KDELR3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.81× lower at baseline in the lines without SNHG18 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.50× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.45× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.48× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.42× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[IQ 1 (drug)]] 5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.69× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.66× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.75× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Lidocaine (hydrochloride) (drug)]] 0.05 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.64× the cells of the other lines | 0.053 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Tolcapone (drug)]] 5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Naproxen (drug)]] 5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.066 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.22× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Salicylic acid (drug)]] 5 µM | C | [[ENSG00000288587]], KDELR3, [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.21× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, -33.1); signed map (-51.6, 9.3). **Vector** length 101, 28.4% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.60 to 10); *COPII-mediated vesicle transport* (reactome, mean cos +0.64 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.71 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -2.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -12.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -8.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -10.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | KDEL endoplasmic reticulum protein retention receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,468,078-38,483,447 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | KDEL endoplasmic reticulum protein retention receptors |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, GLYCOLYSIS, HYPOXIA |
| Reactome | 14 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [O43731](https://www.uniprot.org/uniprotkb/O43731) (ER lumen protein-retaining receptor 3):

> Receptor for the C-terminal sequence motif K-D-E-L that is present on endoplasmic reticulum resident proteins and that mediates their recycling from the Golgi back to the endoplasmic reticulum.

**Summary**, from NCBI Gene [11015](https://www.ncbi.nlm.nih.gov/gene/11015):

> This gene encodes a member of the KDEL endoplasmic reticulum protein retention receptor family. Retention of resident soluble proteins in the lumen of the endoplasmic reticulum (ER) is achieved in both yeast and animal cells by their continual retrieval from the cis-Golgi, or a pre-Golgi compartment. Sorting of these proteins is dependent on a C-terminal tetrapeptide signal, usually lys-asp-glu-leu (KDEL) in animal cells, and his-asp-glu-leu (HDEL) in S. cerevisiae. This process is mediated by …

**Accessions** — [HGNC:6306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6306) · Entrez [11015](https://www.ncbi.nlm.nih.gov/gene/11015) · UniProt [O43731](https://www.uniprot.org/uniprotkb/O43731) · Ensembl [ENSG00000100196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100196)

## Data

Gene col 1886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1886); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1886]; `tensor/DDL_lfc|DDL_z.npy` [1886]; `embed/gene_vectors.npy` [1886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1886 or target_col == 1886). Every well: [[KDELR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDELR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "CCNA2"
type: "gene"
col: 6985
ensembl_id: "ENSG00000145386"
name: "cyclin A2"
location: "4q27"
module: 22
arm: "+"
pooled_cpm: 32.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CCNA2

*cyclin A2* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.15× (z +7.7, q 1e-11, up in 37 of 46 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.61× (z +4.6, q 5e-04, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.382× (z -8.3, q 5e-14, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.519× (z -6.8, q 2e-09, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1]] (+0.94, fdr 7e-06), [[ARHGAP11A]] (+0.93, fdr 7e-06), [[KIF23]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **2.15×** | +7.7 | 1e-11 | 37/46 (HOP62, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.42×** | +5.1 | 8e-05 | 31/48 (HOP62, NCI-H23, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **2.35×** | +4.7 | 5e-04 | 27/47 (J82, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.61×** | +4.6 | 5e-04 | 28/48 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.49×** | +4.0 | 0.007 | 23/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.43×** | +3.7 | 0.017 | 24/44 (PANC-1, SW1417, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.39×** | +3.3 | 0.081 | 22/47 (C-33 A, A-172, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | 1.37× | +3.2 | 0.10 | 20/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 1.34× | +3.1 | 0.12 | 18/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.34× | +3.1 | 0.12 | 20/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.14 | 19/47 (HOP62, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.382×** | -8.3 | 5e-14 | 36/48 (A-172, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.599×** | -7.5 | 1e-11 | 32/48 (A498, H4, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.519×** | -6.8 | 2e-09 | 33/48 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.522×** | -6.8 | 2e-09 | 34/48 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.503×** | -6.5 | 8e-09 | 36/48 (A498, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -5.4 | 6e-06 | 33/48 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.599×** | -5.1 | 2e-05 | 38/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.728×** | -4.7 | 2e-04 | 27/48 (A498, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.739×** | -4.4 | 6e-04 | 23/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.646×** | -4.4 | 8e-04 | 28/48 (COLO 205, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.635×** | -4.3 | 8e-04 | 28/48 (SW 900, Hs 766T, …) | two highest doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.489×** | -3.9 | 0.005 | 25/48 (A498, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **0.492×** | -3.9 | 0.005 | 24/41 (A-427, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.693×** | -3.8 | 0.005 | 22/48 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.008 | 21/48 (RKO, HCT15, …) | two highest doses | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.021 | 25/48 (Hs 766T, NCI-H1792, …) | rises with dose | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.677×** | -3.4 | 0.025 | 22/48 (hTERT-HPNE, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.640×** | -3.3 | 0.027 | 22/48 (HOP62, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.028 | 20/48 (CFPAC-1, SHP-77, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -3.2 | 0.040 | 20/48 (KATO III, NCI-H1573, …) | rises with dose | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.740×** | -3.1 | 0.044 | 15/48 (NCI-H23, NCI-H2347, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.657×** | -3.1 | 0.044 | 21/46 (SW48, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.730×** | -3.0 | 0.063 | 22/48 (H4, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +1.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.2 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.175× (z -19.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -11.5) |
| [[A-172 (line)]] | wt | 35.6 | 0 | 4 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.173× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 68.7 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.200× (z -15.6) |
| [[SNU-1 (line)]] | wt | 45.7 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.141× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0793× (z -10.3) |
| [[H4 (line)]] | wt | 44.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0814× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0347× (z -12.8) |
| [[SHP-77 (line)]] | alt | 48.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.198× (z -9.7) |
| [[LS 180 (line)]] | wt | 36.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.127× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 44.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -9.5) |
| [[C32 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.326× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0583× (z -9.6) |
| [[HOP62 (line)]] | alt | 39.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.8) |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.156× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.131× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.409× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.185× (z -8.5) |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 981 |
| [[ARHGAP11A]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | STRING 715 |
| [[KIF23]] | +0.92 | +0.91 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 914 |
| [[DLGAP5]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | STRING 970 |
| [[KIF11]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 978 |
| [[TPX2]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 954 |
| [[TOP2A]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 982 |
| [[KIF20A]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | STRING 974 |
| [[RACGAP1]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 856 |
| [[BUB1B]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 994 |
| [[BIRC5]] | +0.91 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 956 |
| [[MKI67]] | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 930 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CCNA2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without PIMREG | 0.023 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises CCNA2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.98× lower at baseline in the lines without NEURL1B | 0.079 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[FAM72D]] | C | FAM72D activity raises CCNA2's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | AURKB activity raises CCNA2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without AURKB | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CCNA2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without PBK | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CCNA2's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.61× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[NDC80]] | C | NDC80 activity raises CCNA2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without NDC80 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.946). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.1, -55.3); signed map (-49.0, -42.9). **Vector** length 154, 53.9% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.73 to 48); *E2F targets* (hallmark, mean cos +0.74 to 46); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.75 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | +7.8 | +7.7 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +5.6 | +5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +4.6 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.1 |
|  | [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.6 | +2.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -7.7 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -6.8 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -6.6 | -6.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -4.6 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:121,816,444-121,823,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CCNA, CCN1 |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 57 pathways, smallest: G2 Phase; G2/M DNA replication checkpoint; TP53 Regulates Transcription of Genes Involved in G1 Cell Cycle Arrest |
| Matched by | ensembl_id |

**Function**, from UniProt [P20248](https://www.uniprot.org/uniprotkb/P20248) (Cyclin-A2):

> Essential for the control of the cell cycle at G1/S and G2/M transition. Functions through the formation of specific serine/threonine protein kinase holoenzyme complexes with the cyclin-dependent protein kinases CDK1 or CDK2. The cyclin subunit confers the substrate specificity of these complexes and differentially interacts with and activates CDK1 and CDK2 throughout the cell cycle.

**Summary**, from NCBI Gene [890](https://www.ncbi.nlm.nih.gov/gene/890):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members function as regulators of the cell cycle. This protein binds and activates cyclin-dependent kinase 2 and thus promotes transition through G1/S and G2/M. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:1578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1578) · Entrez [890](https://www.ncbi.nlm.nih.gov/gene/890) · UniProt [P20248](https://www.uniprot.org/uniprotkb/P20248) · Ensembl [ENSG00000145386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145386)

## Data

Gene col 6985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6985); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6985]; `tensor/DDL_lfc|DDL_z.npy` [6985]; `embed/gene_vectors.npy` [6985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6985 or target_col == 6985). Every well: [[CCNA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

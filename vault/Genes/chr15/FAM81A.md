---
symbol: "FAM81A"
type: "gene"
col: 8074
ensembl_id: "ENSG00000157470"
name: "family with sequence similarity 81 member A"
location: "15q22.2"
module: 12
arm: "-"
pooled_cpm: 25.97
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# FAM81A

*family with sequence similarity 81 member A* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.28× (z +21.2, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.746× (z -5.3, q 6e-05, down in 19 of 44 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.790× (z -4.3, q 0.005, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R15B-AS1]] (+0.59, fdr 1e-05), [[TMSB4X]] (+0.54, fdr 5e-05), [[CEACAM16-AS1]] (+0.53, fdr 4e-05); moves opposite to [[CDPF1]] (-0.64, fdr 3e-05), [[MRPL46]] (-0.63, fdr 1e-04), [[NSUN5]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +21.2 | 0e+00 | 42/47 (CFPAC-1, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +17.6 | 0e+00 | 30/34 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +17.1 | 0e+00 | 39/42 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +12.1 | 1e-31 | 35/37 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +11.1 | 2e-26 | 39/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.77×** | +10.4 | 2e-23 | 36/48 (A498, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +9.3 | 1e-18 | 35/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.55×** | +7.9 | 2e-13 | 29/48 (J82, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.7 | 2e-09 | 28/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.44×** | +6.7 | 2e-09 | 23/48 (SK-MEL-2, J82, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +6.0 | 9e-08 | 25/48 (SW480, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +5.2 | 9e-06 | 18/47 (SW480, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.28×** | +4.4 | 6e-04 | 20/46 (SW480, hTERT-HPNE, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 10/48 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.018 | 14/48 (SW1417, CFPAC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **0.746×** | -5.3 | 6e-05 | 19/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -4.3 | 0.005 | 19/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.793×** | -4.2 | 0.005 | 10/48 (A498, NCI-H23, …) | two highest doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -4.0 | 0.010 | 11/35 (SHP-77, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -3.7 | 0.022 | 18/47 (SW480, LS 180, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.870× | -3.6 | 0.030 | 10/49 (PANC-1, SNU-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.812×** | -3.6 | 0.030 | 19/46 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.824×** | -3.5 | 0.032 | 19/47 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.823×** | -3.3 | 0.053 | 11/48 (LS 180, HS-578T, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.707×** | -3.3 | 0.057 | 8/44 (HT-29, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 17.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.03× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 18.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 16.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 31.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.17× (z +9.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.309× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~20% of this change |
| [[H4 (line)]] | wt | 19.1 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0689× (z -13.4) |
| [[SW480 (line)]] | alt | 24.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.3) | — |
| [[A-172 (line)]] | wt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +11.4) | — |
| [[A-427 (line)]] | wt | 21.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 35.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 31.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +10.1) | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.151× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.0) | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[RPMI-7951 (line)]] | alt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 25.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.4) | — |
| [[SW48 (line)]] | wt | 23.9 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0946× (z -10.0) |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*12 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R15B-AS1]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TMSB4X]] | +0.54 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[CEACAM16-AS1]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[DHFR]] | +0.53 | +0.21 / +0.49 | both halves | 7e-04 |  |
| [[TRD-AS1]] | +0.52 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[LYRM1]] | +0.52 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[BHLHE40-AS1]] | +0.51 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[LINC01019]] | +0.50 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[CD302]] | +0.50 | +0.32 / +0.53 | both halves | 1e-04 |  |
| [[ARGLU1]] | +0.49 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[ADGRE3]] | +0.49 | +0.28 / +0.43 | both halves | 3e-04 |  |
| [[TNS2-AS1]] | +0.49 | +0.17 / +0.55 | ⚠ one half (not replicated) | 0.001 |  |

## Genes that move opposite

*88 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDPF1]] | -0.64 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[MRPL46]] | -0.63 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[NSUN5]] | -0.62 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[C18orf21]] | -0.61 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[MYG1]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[BRF2]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | -0.59 | -0.52 / -0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDRG1]] | -0.59 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[ISCA2]] | -0.59 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[ZNF205]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[PREB]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RBMX2]] | -0.58 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[COASY]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM81A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.7, -6.8); signed map (45.5, -6.5). **Vector** length 78.9, 14.6% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +17.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +21.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | +2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.7 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.1 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 81 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:59,372,693-59,523,555 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26690 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBF8](https://www.uniprot.org/uniprotkb/Q8TBF8) (Protein FAM81A):

> Facilitates the interaction and assembly of proteins within the postsynaptic density by promoting the condensation of postsynaptic proteins via liquid-liquid phase separation. Required for neuronal activity. Accumulation at the postsynaptic density results in enlargement of dendritic spines.

**Summary**, from NCBI Gene [145773](https://www.ncbi.nlm.nih.gov/gene/145773):

> Predicted to enable molecular condensate scaffold activity. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28379) · Entrez [145773](https://www.ncbi.nlm.nih.gov/gene/145773) · UniProt [Q8TBF8](https://www.uniprot.org/uniprotkb/Q8TBF8) · Ensembl [ENSG00000157470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157470)

## Data

Gene col 8074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8074); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8074]; `tensor/DDL_lfc|DDL_z.npy` [8074]; `embed/gene_vectors.npy` [8074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8074 or target_col == 8074). Every well: [[FAM81A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM81A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

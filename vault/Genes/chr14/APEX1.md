---
symbol: "APEX1"
type: "gene"
col: 2029
ensembl_id: "ENSG00000100823"
name: "apurinic/apyrimidinic endodeoxyribonuclease 1"
location: "14q11.2"
module: 20
arm: "+"
pooled_cpm: 26.78
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020", "written"]
generated_by: "tahoemap"
---

# APEX1

*apurinic/apyrimidinic endodeoxyribonuclease 1* — 14q11.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> APEX1 encodes APE1/Ref-1: the main AP endonuclease of base-excision repair and, separately, a redox cofactor that keeps other transcription factors able to bind DNA.

## What it is

APE1 incises the DNA backbone at abasic sites left by glycosylases, the committed step of base-excision repair. It is abundant, largely nuclear, and essential: homozygous loss is early-embryonic lethal in mice. Its second function was discovered independently, as Ref-1, an activity that restores DNA binding to oxidised AP-1, and was later extended to NF-κB, HIF-1α, STAT3 and p53 — redox chemistry, not sequence-specific DNA binding of its own. The two activities are separable: APX3330 blocks the redox function and spares the endonuclease.

## What is uncertain

APE1 is not a sequence-specific transcription factor, so its assigned regulon is borrowed from the factors it reduces, and a high inferred activity may be reporting AP-1, NF-κB or HIF-1α output instead — a limitation of target-based activity inference applied to a cofactor. How much of the redox function operates at endogenous protein levels, rather than in vitro on oxidised substrate, remains argued. The repair activity itself is not in doubt.

## References

- Demple et al., 1991, PNAS — cloned the major human apurinic/apyrimidinic endonuclease.
- Xanthoudakis and Curran, 1992, EMBO Journal — identified Ref-1 as a nuclear factor that restores AP-1 DNA binding.
- Xanthoudakis et al., 1996, PNAS — Apex-null mouse embryos die early, establishing the gene as essential.
- Jayaraman et al., 1997, Genes and Development — Ref-1 stimulates the DNA binding and transcriptional activity of p53 in vitro.
- Gaiddon et al., 1999, EMBO Journal — Ref-1 associates with p53 in cells, and is required for its transactivation and pro-apoptotic function.
- Tell et al., 2009, Antioxidants and Redox Signaling — review of APE1/Ref-1's dual repair and redox roles.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.93× (z +14.5, q 6e-45, up in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.72× (z +7.1, q 2e-10, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.701× (z -6.8, q 4e-09, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS30]] (+0.63, fdr 7e-06), [[PHB2]] (+0.63, fdr 7e-06), [[ZZZ3]] (+0.61, fdr 7e-06); moves opposite to [[IER5]] (-0.58, fdr 1e-05), [[SRSF9]] (-0.53, fdr 2e-05, ⚠ SRSF9 in the vector space only through flagged drug-doses), [[CCNYL1]] (-0.52, fdr 2e-05), [[COX17]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNK6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +14.5 | 6e-45 | 42/45 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +12.1 | 3e-31 | 35/38 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +8.0 | 3e-13 | 35/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.72×** | +7.1 | 2e-10 | 39/47 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.9 | 4e-07 | 28/48 (C32, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.2 | 1e-05 | 32/46 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.9 | 7e-05 | 29/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.5 | 5e-04 | 20/48 (NCI-H2347, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.86×** | +4.4 | 7e-04 | 23/46 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.9 | 0.005 | 24/46 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.7 | 0.009 | 0/48 | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.27×** | +3.2 | 0.059 | 13/47 (A498, HepG2/C3A, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.095 | 19/45 (SW 900, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.701×** | -6.8 | 4e-09 | 34/48 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.751×** | -3.9 | 0.025 | 20/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.613×** | -3.5 | 0.095 | 20/46 (Panc 03.27, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.783× | -3.3 | 0.12 | 19/47 (RKO, SW48, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.785× | -3.2 | 0.15 | 18/47 (SW48, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -3.2 | 0.15 | 12/48 (SW 900, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.797× | -3.1 | 0.16 | 15/46 (BT-474, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.801× | -3.0 | 0.17 | 19/47 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 22.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +9.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 43.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.404× (z -8.9) |
| [[CHP-212 (line)]] | wt | 48.7 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0584× (z -11.2) |
| [[J82 (line)]] | alt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 21.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 31.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.38× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +11.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 46.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.3) |
| [[SW480 (line)]] | alt | 31.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.4) |
| [[A549 (line)]] | wt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +11.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS30]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PHB2]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ZZZ3]] | +0.61 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LRPPRC]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ENOPH1]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[DDX54]] | +0.60 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[UTP18]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SPG21]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[EIF4B]] | +0.59 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[PDCL3]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[EIF3C]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MRPS35]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SRSF9]] ⚠ | -0.53 | -0.48 / -0.50 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCNYL1]] | -0.52 | -0.53 / -0.49 | both halves | 2e-05 |  |
| [[COX17]] | -0.51 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[KCTD11]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TRIOBP]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PFN1]] | -0.50 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[TUBB4B]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[DRAP1]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SEC61G]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ARID3A]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[KCNK6]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SERTAD1]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK6]] | B | KCNK6 activity lowers APEX1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without KCNK6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.4, -13.7); signed map (-21.7, -46.0). **Vector** length 83.1, 18.4% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.50 to 11); *GTP hydrolysis and joining of the 60S ribosomal subunit* (reactome, mean cos +0.50 to 11); *Eukaryotic Translation Elongation* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.5 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | apurinic/apyrimidinic endodeoxyribonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,455,191-20,457,772 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APE, REF1, HAP1, APX, APEN, REF-1, APE-1, APE1; previously APEX |
| Gene groups (HGNC) | SET complex; Endoribonucleases |
| Hallmark sets | FATTY_ACID_METABOLISM, MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Resolution of AP sites via the single-nucleotide replacement pathway; POLB-Dependent Long Patch Base Excision Repair; Displacement of DNA glycosylase by APEX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P27695](https://www.uniprot.org/uniprotkb/P27695) (DNA repair nuclease/redox regulator APEX1):

> Multifunctional protein that plays a central role in the cellular response to oxidative stress. The two major activities of APEX1 are DNA repair and redox regulation of transcriptional factors. Functions as an apurinic/apyrimidinic (AP) endodeoxyribonuclease in the base excision repair (BER) pathway of DNA lesions induced by oxidative and alkylating agents. Initiates repair of AP sites in DNA by catalyzing hydrolytic incision of the phosphodiester backbone immediately adjacent to the damage, …

**Summary**, from NCBI Gene [328](https://www.ncbi.nlm.nih.gov/gene/328):

> The APEX gene encodes the major AP endonuclease in human cells. It encodes the APEX endonuclease, a DNA repair enzyme with apurinic/apyrimidinic (AP) activity. Such AP activity sites occur frequently in DNA molecules by spontaneous hydrolysis, by DNA damaging agents or by DNA glycosylases that remove specific abnormal bases. The AP sites are the most frequent pre-mutagenic lesions that can prevent normal DNA replication. Splice variants have been found for this gene; all encode the same …

**Accessions** — [HGNC:587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:587) · Entrez [328](https://www.ncbi.nlm.nih.gov/gene/328) · UniProt [P27695](https://www.uniprot.org/uniprotkb/P27695) · Ensembl [ENSG00000100823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100823)

## Data

Gene col 2029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2029); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2029]; `tensor/DDL_lfc|DDL_z.npy` [2029]; `embed/gene_vectors.npy` [2029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2029 or target_col == 2029). Every well: [[APEX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/APEX1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
